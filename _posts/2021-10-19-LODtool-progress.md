---
layout: post
title: LOD Tool Progress - Freshers Flu Edition
tags:
  - professional-practice
description: >

hero: /uploads/hero_LODtool_update.jpg
overlay: purple
published: true
---

# Working when you're sick is difficult
Not to speak the obvious with the title, but dealing with staying on top of things when you're not feeling 100% can be really difficult, both mentally and physically. For me, it was mostly the struggle of needing to know I'm on track to finish my projects before the deadline. Because I'm still quite new to python, having no rough estimate of when the tool could be finished by did stress me out a bit. 

## A surprising outcome
I've now lost a grand total of 5 working days either setting up my workspace at university (we've recently changed rooms and I had to move my old computer to the new room) or being sick. That's a long time in the production world. 

We're now at the beginning of week 3 of university and I can proudly say that 95% of the tool functionality is implemented. All there really is to do now is to make a pretty UI for it, which I'm hoping to get done by the end of this week, or early next week. I've recently had to follow a very strict **no work in the weekends** policy, enforced by my thoughtful partner whom already thinks I'm working too much. Maybe that really is the case.

## The Mysterious get_num_sections() Function
I had been looking for a way to get the triangle count for each LOD for ages. I tried getting the number of polygons first, then based on that calculating the number of triangles. That didn't work. Tried the same with vertices. Same situation.

**But then**, the magical get_num_sections() function appeared out of nowhere to save the day. Well not really - I desperately googled until I found it. **Regardless**, this then allowed me to use the get_section_from_static_mesh() function, which returns an array of information about the static mesh such as triangles, vertices, etc.

Here's the code that saved me a breakdown:
``` python
def get_lod_triangles(static_mesh):
    lod_details = []

    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)
    unreal.EditorStaticMeshLibrary.set_allow_cpu_access(static_mesh, True)

    for lod in range(lod_no):
        triangle_count = 0
        num_sections = static_mesh.get_num_sections(lod)
        for section_number in range(num_sections):
            section_data = unreal.ProceduralMeshLibrary.get_section_from_static_mesh(
                static_mesh, lod, section_number
            )
            triangle_count += len(section_data[1])
        lod_detail_dict = {"lod_number": lod, "triangle_count": triangle_count / 3}
        lod_details.append(lod_detail_dict)

    for lod_detail_dict in lod_details:
        print(
            f"LOD number {lod_detail_dict.get('lod_number')} has {lod_detail_dict.get('triangle_count')} triangles.\n"
        )

    return lod_details
```


## A new way to manage projects
Working on two projects at once can seem easy at first, but once you start getting more and more into each one of them, it can get overwhelming. So I was faced with the challenge of sorting my messy head out - but how? 

At first I thought I was limited to google docs or my bullet journal, but then I discovered **notion**. I made a very simple system - divide tasks by projects and give them relevant types to describe the tool I need to use to complete the task. And so was born **the ultimate head decluttering system**.

![](/uploads/notion.jpg)

This works really well for me because you can sort tasks by project, type and whether or not it has been completed. That way I can also keep track of what I've done so far, so I don't end up thinking I haven't been productive.

## Dealing with the lack of resources
Unreal Engine 4 itself is admirably well documented. Its python API however.. not so much. It took me a good minute to understand how to read said docs, and how to work with certain classes, but in the end I decyphered it (to some extent). 

Being on a Game **Art** course and choosing to do Technical Art, while it definitely was the right decision, can also be challenging at times. There isn't really a way for me to bounce ideas off people or get any feedback, but there's also upsides to it. I can wander around a room full of ridiculously talented people, admire their art and clear my head talking to them about anything but my work, and that usually leads to a fresh perspective when I return to my desk. 

## So What's Next?
My goal now is to start making my code work with Editor Utility Widgets, in order to make a UI. I figured it would be easier to make it directly in UE4 rather than through code, as the visual aspect of it will be a massive help. I know presentation is just as important as the functionality with this project - the user needs to be able to use the tool intuitively, regardless of their knowledge of the code behind it.  

### Thanks for reading!