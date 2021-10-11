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

I wasn't exactly aware that you need to enable some extra plugins in Unreal to be able to run Python scripts, but we live and we learn. 

![script](/uploads/plugins.JPG)

After that, all you need to do is go into the **context menu** and select **File**>**Python**>**Execute Python Script**. If you're lucky enough and your script doesn't run into any runtime issues, you should be able to see it doing its thing in the **Output Log** that you can access in the same context menu, by selecting **Window**>**Developer Tools**>**Output Log**. 

![contextmenu](/uploads/python_context_menu.jpg)
![contextmenu](/uploads/output.jpg)

## The First Function

I decided to start the projects by making a function that takes the number of LODs a mesh has from the engine, and outputs it neatly next to the mesh name.

```python
    def check_lods(static_mesh):
        lod_no = unreal.EditorStaticMeshLibrary.get_lod_count(static_mesh)
        print(static_mesh.get_name())
        print(f"current LOD count: {lod_no}")
```
Surprisingly enough, this just worked straight away. 

## Structure
I think as a beginner, project structure is something I really struggle with. For now, the plan is to keep making functions and testing that they work as I go, and then work on a UI for the tool and potentially some extra functionality. The most important thing is to first get all the data I require from the engine and then be able to put it all into a spreadsheet. I hear technical artists really like spreadsheets so I'm gonna join the fun.

## Preferred outcomes and goals
My main goal with this project is to get more comfortable using Python and to get used to the Unreal API, as I'm sure I'll be using it in the future too. Beyond that, I want to test my ability to time manage a project that I have no rough estimate how long it's actually going to take, given that I have to learn so many new things. 

Another goal of mine is to finally keep my development diary (aka this blog) up to date with every issue, fix or implementation that I make.

My next post will be about starting the Shader Museum project, as I wish to work on both at the same time, mainly to be able to take a break from code when I need it, or take a break from shader spaghetti nodes.

