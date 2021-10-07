---
layout: page
title: About
permalink: /about/
published: true
---

<div class="page" markdown="1">

{% capture page_subtitle %}
<img
    class="me"
    alt="{{ author.name }}"
    src="{{ site.author.photo | relative_url }}"
    srcset="{{ site.author.photo2x | relative_url }} 2x"
/>
{% endcapture %}

{% include page/title.html title=page.title subtitle=page_subtitle %}

I'm a 21 year old studying Game Art at De Montfort University in Leicester, UK. I do both 2D and 3D work, so you can expect to see bit of both here.

## Tools I Use

* Modeling: 3DSMax
* Texturing: Photoshop / Substance Painter
* Real-time rendering: Marmoset Toolbag / Unreal Engine 4
* Engines: Unreal Engine 4 / Unity

</div>
