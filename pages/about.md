---
permalink: /
title: ""
excerpt: "Yuchuan Deng — Ph.D. student at Renmin University of China working on multimodal large language models and video understanding."
author_profile: true
hide_title: true
redirect_from:
  - /about/
  - /about.html
---

<div class="profile-intro" markdown="1">

I am a Ph.D. student at the [AI & Media Computing Lab (AIMC Lab)](https://ruc-aimc-lab.github.io/), [Renmin University of China (RUC)](https://www.ruc.edu.cn/), supervised by [Prof. Xirong Li](https://lixirong.net/).

I received my **B.Eng. in Computer Science and Technology** from [Sichuan University](https://cs.scu.edu.cn/), where I was advised by [Prof. Qijun Zhao](http://www.scubrl.org/qjzhao).

My research interests primarily include:
- **Multimodal LLMs:** efficient inference and post-training for MLLMs.
- **Medical Multimodal AI:** multimodal reasoning and few-shot learning for medical image understanding.

</div>

<section class="academic-section" id="news">
  <h2>News</h2>
  <div class="news-list">
    <div class="news-row"><time>Jul 2026</time><div>Released our preprint on <strong>few-shot medical image segmentation benchmarking</strong>.</div></div>
    <div class="news-row"><time>Apr 2026</time><div>Released <strong>Fundus-R1</strong>, a fundus-reading MLLM trained with knowledge-aware reasoning on public data.</div></div>
    <div class="news-row"><time>2026</time><div>Our work on <strong>dynamic memorization and exploration for small VLMs</strong> appears at <strong>ICLR 2026</strong>.</div></div>
    <div class="news-row"><time>Sep 7, 2025</time><div>Started my Ph.D. at <strong>Renmin University of China</strong> under the supervision of Prof. Xirong Li.</div></div>
    <div class="news-row"><time>Jun 28, 2025</time><div>Graduated from Sichuan University and was honored as an <strong>Outstanding Graduate of Sichuan Province</strong>.</div></div>
    <div class="news-row"><time>Mar 21, 2025</time><div>Our paper on <strong>text-based person search</strong> was accepted to <strong>ICME 2025</strong>.</div></div>
    <div class="news-row"><time>Mar 1, 2025</time><div>Started a research internship at <strong>Baidu</strong>, focusing on large-scale model data.</div></div>
  </div>
</section>

<section class="academic-section" id="publications">
  <div class="section-title-row">
    <h2>Publications</h2>
    <a class="section-more" href="/publications/">Full list</a>
  </div>
  <p class="section-note">* Equal contribution.</p>
  <div class="publication-list">
    {% for pub in site.data.publications %}
      {% include publication-card.html pub=pub %}
    {% endfor %}
  </div>
</section>

<section class="academic-section" id="education">
  <h2>Education</h2>
  <div class="simple-list">
    <div class="simple-row">
      <div>
        <strong>Renmin University of China</strong>
        <span>Ph.D. in Computer Science and Technology</span>
      </div>
      <time>Sep. 2025 – Present</time>
    </div>
    <div class="simple-row">
      <div>
        <strong>Sichuan University</strong>
        <span>B.Eng. in Computer Science and Technology</span>
      </div>
      <time>Sep. 2021 – Jun. 2025</time>
    </div>
  </div>
</section>

<section class="academic-section" id="patents">
  <h2>Patents</h2>
  <div class="text-entry-list">
    <div class="text-entry">
      <strong>Text-Driven Pedestrian Retrieval Method and System Based on SAM.</strong>
      <span><strong>Yuchuan Deng</strong>, Qijun Zhao, Keran Fu, Libin Ye, Zongyong Deng.</span>
      <em>Patent No. ZL 2024 1 042542.5</em>
    </div>
    <div class="text-entry">
      <strong>Adaptive Non-Contact Yak Weight Analysis Method and System Based on SAM.</strong>
      <span>Sonam Jianzhuo, Qijun Zhao, Nima Zhaxi, <strong>Yuchuan Deng</strong>, Xinyu Yang.</span>
      <em>Patent No. ZL 2024 1 0520466.8</em>
    </div>
    <div class="text-entry">
      <strong>An Intelligent Recognition Device.</strong>
      <span>Keyun Li, <strong>Yuchuan Deng</strong>, Qijun Zhao, Guoying Deng.</span>
      <em>Application No. 2024209943132</em>
    </div>
  </div>
</section>

<section class="academic-section" id="service">
  <h2>Service</h2>
  <h3 class="subsection-title">Teaching Assistant</h3>
  <div class="teaching-list">
    {% for item in site.data.teaching %}
      {% include teaching-item.html item=item %}
    {% endfor %}
  </div>
</section>

<section class="academic-section" id="activities">
  <h2>Activities</h2>
  <div class="simple-list">
    <div class="simple-row">
      <div>
        <strong>President, Artificial Intelligence Association</strong>
        <span>Sichuan University</span>
      </div>
      <time>Jun. 2023 – Jul. 2024</time>
    </div>
  </div>
</section>
