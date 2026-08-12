---
permalink: /
title: "Yuchuan Deng"
excerpt: "Yuchuan Deng — Ph.D. student at Renmin University of China working on multimodal large language models and video understanding."
author_profile: true
hide_title: true
redirect_from:
  - /about/
  - /about.html
---

<div class="home-intro">
  <div class="home-intro__eyebrow">Ph.D. Student · Multimodal Learning</div>
  <h1 class="home-intro__title">Hi, I’m Yuchuan Deng.</h1>
  <p class="home-intro__lead">I am a Ph.D. student at the <a href="https://ruc-aimc-lab.github.io/">AI & Media Computing Lab (AIMC Lab)</a>, <a href="https://www.ruc.edu.cn/">Renmin University of China (RUC)</a>, supervised by <a href="https://lixirong.net/">Prof. Xirong Li</a>.</p>
  <p>I received my <strong>B.Eng. in Computer Science and Technology</strong> from <a href="https://cs.scu.edu.cn/">Sichuan University</a>, where I was advised by <a href="http://www.scubrl.org/qjzhao">Prof. Qijun Zhao</a>.</p>
  <div class="interest-list" aria-label="Research interests">
    <span>Resource-Efficient Multimodal LLMs</span>
    <span>Omni-Modal & Video Reasoning</span>
    <span>Medical Multimodal AI</span>
  </div>
</div>

<section class="home-section">
  <div class="section-heading">
    <h2>News</h2>
  </div>
  <div class="news-list">
    <div class="news-item"><time>Jul 2026</time><p>Released our preprint on <strong>few-shot medical image segmentation benchmarking</strong>.</p></div>
    <div class="news-item"><time>Apr 2026</time><p>Released <strong>Fundus-R1</strong>, a fundus-reading MLLM trained with knowledge-aware reasoning on public data.</p></div>
    <div class="news-item"><time>2026</time><p>Our work on <strong>dynamic memorization and exploration for small VLMs</strong> appears at <strong>ICLR 2026</strong>.</p></div>
    <div class="news-item"><time>Sep 7, 2025</time><p>Started my Ph.D. at <strong>Renmin University of China</strong> under the supervision of Prof. Xirong Li.</p></div>
    <div class="news-item"><time>Jun 28, 2025</time><p>Graduated from Sichuan University and was honored as an <strong>Outstanding Graduate of Sichuan Province</strong>.</p></div>
    <div class="news-item"><time>Mar 21, 2025</time><p>Our paper on <strong>text-based person search</strong> was accepted to <strong>ICME 2025</strong>.</p></div>
    <div class="news-item"><time>Mar 1, 2025</time><p>Started a research internship at <strong>Baidu</strong>, focusing on large-scale model data.</p></div>
  </div>
</section>

<section class="home-section">
  <div class="section-heading"><h2>Education</h2></div>
  <div class="education-grid">
    <article class="education-card">
      <div class="education-card__degree">Ph.D. in Computer Science and Technology</div>
      <div class="education-card__school">Renmin University of China</div>
      <div class="education-card__meta">Beijing, China · Sep. 2025 – Present</div>
    </article>
    <article class="education-card">
      <div class="education-card__degree">B.Eng. in Computer Science and Technology</div>
      <div class="education-card__school">Sichuan University</div>
      <div class="education-card__meta">Chengdu, China · Sep. 2021 – Jun. 2025</div>
    </article>
  </div>
</section>

<section class="home-section" id="publications">
  <div class="section-heading section-heading--with-link">
    <h2>Publications</h2>
    <a href="/publications/">View all</a>
  </div>
  <div class="publication-list">
    {% for pub in site.data.publications %}
      {% include publication-card.html pub=pub %}
    {% endfor %}
  </div>
</section>

<section class="home-section">
  <div class="section-heading"><h2>Patents</h2></div>
  <div class="compact-card-list">
    <article class="compact-card">
      <h3>Text-Driven Pedestrian Retrieval Method and System Based on SAM</h3>
      <p><strong>Yuchuan Deng</strong>, Qijun Zhao, Keran Fu, Libin Ye, Zongyong Deng</p>
      <span>Patent No. ZL 2024 1 042542.5</span>
    </article>
    <article class="compact-card">
      <h3>Adaptive Non-Contact Yak Weight Analysis Method and System Based on SAM</h3>
      <p>Sonam Jianzhuo, Qijun Zhao, Nima Zhaxi, <strong>Yuchuan Deng</strong>, Xinyu Yang</p>
      <span>Patent No. ZL 2024 1 0520466.8</span>
    </article>
    <article class="compact-card">
      <h3>An Intelligent Recognition Device</h3>
      <p>Keyun Li, <strong>Yuchuan Deng</strong>, Qijun Zhao, Guoying Deng</p>
      <span>Application No. 2024209943132</span>
    </article>
  </div>
</section>

<section class="home-section" id="service">
  <div class="section-heading"><h2>Service</h2></div>
  <h3 class="section-subtitle">Teaching Assistant</h3>
  <div class="teaching-list">
    {% for item in site.data.teaching %}
      {% include teaching-item.html item=item %}
    {% endfor %}
  </div>
</section>

<section class="home-section home-section--last">
  <div class="section-heading"><h2>Activities</h2></div>
  <div class="activity-row">
    <div>
      <strong>President, Artificial Intelligence Association</strong>
      <span>Sichuan University</span>
    </div>
    <time>Jun. 2023 – Jul. 2024</time>
  </div>
</section>
