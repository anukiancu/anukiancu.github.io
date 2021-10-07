---
layout: post
title: First look at the LOD tool project 
tags:
  - professional-practice
description: >
  Example text
hero: /uploads/code.JPG
overlay: purple
published: true
---

# A python newbie's approach

## Why I chose the project

Going into this project was a bit of a leap of faith. Faith that I'll be able to pick up a new programming language and use it with the Unreal Enginge Python API to create a tool according to the project brief.

 All in all, I'm more than willing to put in all the effort it will take to teach myself this stuff now, as I know it will be really helpful knowledge to have before going into the industry. I had a quick chat with someone the other day, and they said something among the lines of "If you're a good technical artist, I can basically guarantee you a job". Needless to say, that really motivated me.

## Setup

Due to the restrictions university enforced on all campus computers, I ran into a million issues while setting up for the project. Tech support was amazing and stayed by my side during what should've been a straight-forward process (installing git, Visual Studio Code, poetry etc.), but ended up taking such a long time and a lot of brain power for troubleshooting. 

It's all working now though, and I ***really*** hope I won't need to ask for more help, because I'm sure every time Craig from IT sees my purple hair he wants to run away.

## Getting the script to run in UE4

I wasn't exactly aware that you need to enable some extra pluggins in Unreal to be able to run Python scripts, but we live and we learn. 

![script](/uploads/plugins.JPG)

After that, all you need to do is go into the **context menu** and select **File**>**Python**>**Execute Python Script**. If you're lucky enough and your script doesn't run into any runtime issues, you should be able to see it doing its thing in the **Output Log** that you can access in the same context menu, by selecting **Window**>**Developer Tools**>**Output Log**. 

![Python <](/uploads/python_context_menu.jpg)
![Python >](/uploads/output.jpg)

## The First Function

I decided to start the projects by making a function that takes the number of LODs a mesh has from the engine, and outputs it neatly next to the mesh name.

```python
    def check_lods(static_mesh):
    lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)
    print(static_mesh.get_name())
    print(f"current LOD count: {lod_no}")
```
This was surprisingly low effort. But if it works it works.
