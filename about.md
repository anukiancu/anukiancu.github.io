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

I'm a 21 year old studying Game Art at De Montfort University. My main focus is Technical Art, but thanks to my art background I am also proficient in 3D software and the 3D development pipeline.

## Tools I Use

* Engines: Unreal Engine 4 / Unity
* Programming Languages: Python, MAXScript, Blueprints
* Modeling: 3DSMax, zBrush
* Texturing: Photoshop / Substance Painter/ Substance Designer
* Real-time rendering: Marmoset Toolbag / Unreal Engine 4


</div>
