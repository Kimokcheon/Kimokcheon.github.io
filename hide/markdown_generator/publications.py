# coding: utf-8
import os
import re
import argparse
import time
import json
from datetime import datetime
import pandas as pd
from slugify import slugify

# --------- Utils ----------
def html_escape(text: str) -> str:
    if text is None:
        return ""
    table = {"&": "&amp;", '"': "&quot;", "'": "&apos;"}
    s = str(text)
    return "".join(table.get(c, c) for c in s)

def validate_date_or_default(year: str) -> str:
    """
    生成 YYYY-MM-DD。Scholar 多为年份，缺月日则用 01-01 占位。
    """
    y = str(year).strip()
    if not y or not y.isdigit():
        y = datetime.now().strftime("%Y")
    return f"{int(y):04d}-01-01"

def pick(s, *keys, default=""):
    for k in keys:
        if s.get(k):
            return s.get(k)
    return default

def build_citation(authors, title, venue, year):
    # 简洁通用的推荐引用格式
    a = authors or ""
    t = title or ""
    v = venue or ""
    y = str(year or "").strip()
    parts = [p for p in [a, t, v, y] if p]
    return ". ".join(parts) + "."

def ensure_dir(p):
    os.makedirs(p, exist_ok=True)

# --------- SerpAPI 路线（更稳） ----------
def fetch_via_serpapi(user_id, api_key):
    import requests
    base = "https://serpapi.com/search.json"
    # 第一次请求
    params = {
        "engine": "google_scholar_author",
        "author_id": user_id,
        "api_key": api_key,
        "sort": "pubdate"  # 按时间
    }
    papers = []
    while True:
        r = requests.get(base, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        papers.extend(data.get("articles", []))
        nxt = data.get("serpapi_pagination", {}).get("next")
        if not nxt:
            break
        # 下一页直接请求 next 链接
        r = requests.get(nxt, timeout=30)
        r.raise_for_status()
        data = r.json()
        papers.extend(data.get("articles", []))
        if not data.get("serpapi_pagination", {}).get("next"):
            break
    return papers

# --------- Scholarly 路线（免费） ----------
def fetch_via_scholarly(user_id):
    from scholarly import scholarly, ProxyGenerator

    # 可选代理（被风控时建议配置 Tor/隧道）
    # pg = ProxyGenerator()
    # pg.FreeProxies()
    # scholarly.use_proxy(pg)

    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["publications"])

    # 再填充每篇的详细字段
    pubs = []
    for p in author.get("publications", []):
        try:
            filled = scholarly.fill(p)
            pubs.append(filled)
            time.sleep(0.7)  # 轻微限速，降低被封概率
        except Exception:
            continue
    return pubs

# --------- 转 TSV ----------
def pubs_to_tsv_rows_from_serpapi(arts):
    rows = []
    for a in arts:
        title = a.get("title", "")
        year  = a.get("year") or ""
        venue = pick(a, "publication", default="")
        url   = pick(a, "link", default="")
        authors = ", ".join([au.get("name","") for au in a.get("authors", [])]) if a.get("authors") else ""
        excerpt = a.get("snippet") or ""
        pub_date = validate_date_or_default(year)
        url_slug = slugify(title)[:80] if title else f"paper-{year}"
        site_url = pick(a, "result_id", default="")  # 无则留空
        citation = build_citation(authors, title, venue, year)

        rows.append({
            "pub_date": pub_date,
            "title": title,
            "venue": venue,
            "excerpt": excerpt,
            "citation": citation,
            "site_url": site_url,
            "paper_url": url,
            "url_slug": url_slug
        })
    return rows

def pubs_to_tsv_rows_from_scholarly(pubs):
    rows = []
    for p in pubs:
        bib = p.get("bib", {})
        title = bib.get("title", "")
        year  = bib.get("pub_year") or bib.get("year") or ""
        # venue 可能在 journal / booktitle / venue
        venue = pick(bib, "venue", "journal", "booktitle", default="")
        authors = ", ".join(bib.get("author", [])) if isinstance(bib.get("author", []), list) else bib.get("author", "")
        excerpt = bib.get("abstract", "") or ""
        pub_date = validate_date_or_default(year)
        url_slug = slugify(title)[:80] if title else f"paper-{year}"
        # paper_url 优先用 eprint / url；否则给 scholar 链接
        paper_url = pick(bib, "eprint", "url", default=p.get("eprint_url", ""))
        site_url  = p.get("pub_url", "") or p.get("author_pub_id", "")
        citation  = build_citation(authors, title, venue, year)

        rows.append({
            "pub_date": pub_date,
            "title": title,
            "venue": venue,
            "excerpt": excerpt,
            "citation": citation,
            "site_url": site_url,
            "paper_url": paper_url,
            "url_slug": url_slug
        })
    return rows

# --------- 生成 Markdown ----------
def dump_markdown_from_tsv(df: pd.DataFrame, out_dir: str):
    ensure_dir(out_dir)
    for _, item in df.iterrows():
        pub_date = item["pub_date"]
        title    = item["title"]
        venue    = item["venue"]
        excerpt  = item.get("excerpt", "")
        citation = item["citation"]
        site_url = item.get("site_url", "")
        paper_url= item.get("paper_url", "")
        url_slug = slugify(item.get("url_slug", "")) or "paper"

        md_filename  = f"{pub_date}-{url_slug}.md"
        html_filename= f"{pub_date}-{url_slug}"

        md = []
        md.append("---")
        md.append(f'title: "{html_escape(title)}"')
        md.append("collection: publications")
        md.append(f"permalink: /publication/{html_escape(html_filename)}")
        if excerpt:
            md.append(f"excerpt: '{html_escape(excerpt)}'")
        md.append(f"date: {pub_date}")
        md.append(f"venue: '{html_escape(venue)}'")
        if paper_url:
            md.append(f"paperurl: '{paper_url}'")
        md.append(f"citation: '{html_escape(citation)}'")
        md.append("---\n")

        if paper_url:
            md.append(f"<a href='{paper_url}'>Download paper here</a>\n")
        if excerpt:
            md.append(f"{html_escape(excerpt)}\n")
        if citation:
            md.append(f"Recommended citation: {citation}")

        out_path = os.path.join(out_dir, md_filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(md))
        print(f"[OK] {out_path}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user_id", default="hG1Gj4QAAAAJ", help="Google Scholar user id, e.g., hG1Gj4QAAAAJ")
    ap.add_argument("--out_tsv", default="C:\\Users\\kimokcheon\\Documents\\Kimokcheon.github.io\\markdown_generator\\publications.tsv", help="Output TSV path")
    ap.add_argument("--out_dir", default="C:\\Users\\kimokcheon\\Documents\\Kimokcheon.github.io\\_publications", help="Markdown output dir")
    args = ap.parse_args()

    # 优先 SerpAPI（若配置了），否则 scholarly
    api_key = os.environ.get("SERPAPI_API_KEY", "").strip()
    if api_key:
        print("[INFO] Using SerpAPI")
        arts = fetch_via_serpapi(args.user_id, api_key)
        rows = pubs_to_tsv_rows_from_serpapi(arts)
    else:
        print("[INFO] Using scholarly (free). If blocked, add proxies or set SERPAPI_API_KEY.")
        pubs = fetch_via_scholarly(args.user_id)
        rows = pubs_to_tsv_rows_from_scholarly(pubs)

    # 生成 TSV
    df = pd.DataFrame(rows, columns=[
        "pub_date","title","venue","excerpt","citation","site_url","paper_url","url_slug"
    ])
    # 去重（按 title+pub_date）
    if not df.empty:
        df = df.drop_duplicates(subset=["title","pub_date"], keep="first")
    df.to_csv(args.out_tsv, sep="\t", index=False, encoding="utf-8")
    print(f"[OK] TSV saved to {args.out_tsv}")

    # 生成 Markdown
    dump_markdown_from_tsv(df, args.out_dir)

if __name__ == "__main__":
    main()
