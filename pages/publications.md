---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<div class="archive-intro">A complete list of publications. * Equal contribution.</div>

<div class="publication-list publication-list--standalone">
{% for pub in site.data.publications %}
  {% include publication-card.html pub=pub %}
{% endfor %}
</div>
