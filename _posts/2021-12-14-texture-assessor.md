---
layout: post
title: Side Project - Texture Assessor Tool
tags:
  - professional-practice
description: >

hero: /uploads/texture_assessor.png
overlay: purple
published: true
---

A couple of days ago a friend of mine reached out to me with an idea: a tool that lets you select a material in UE4, and tells you the name and size of all the textures used by it. I thought that could make a great little project to wind down in the evening, so I got to it straight away.

Here's the code I wrote to make it work:

```python
import unreal
import re

selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

for sa in selected_assets:
    if sa.get_class().get_name() == "Material":
        textures = unreal.MaterialEditingLibrary.get_used_textures(sa)
        x = []
        y = []

        for texture in textures:
            sizeX = unreal.Texture2D.blueprint_get_size_x(texture)
            x.append(sizeX)
            sizeY = unreal.Texture2D.blueprint_get_size_y(texture)
            y.append(sizeY)

            texture_path = re.match(r"<Object ('.*?')", str(texture)).group(1)
            texture_name = texture_path.split("/")[-1].split(".")[-1].strip("'")

            print(f"{texture_name}: {sizeX}x{sizeY}")

        final_sizeX = sum(x)
        final_sizeY = sum(y)

        print(f"Total texture size: {final_sizeX}x{final_sizeY}")
```
I used regular expressions to output the name of the texture correctly to the user, as before it would show the path of the texture and the memory address as well.

Here's how it works in engine:
<video autoplay loop muted playsinline>
  <source src="/uploads/texture_assessor_demo.mp4" type="video/mp4">
</video>

That's it! Tool shipped the same night, friend was happy, and I got to experiment with a new concept (regular expressions). I wonder what my next project will be. I will be taking a break during Christmas, but hope to see you on here again soon! 