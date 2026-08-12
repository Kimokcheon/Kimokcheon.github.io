---
layout: single
title: "Publications"
permalink: /publications/
author_profile: true
---

<div class="page-lead">Selected publications and preprints. My name is shown in <strong>bold</strong>.</div>

<div class="publication-list publication-list--standalone">
  {% for pub in site.data.publications %}
    {% include publication-card.html pub=pub %}
  {% endfor %}
</div>
