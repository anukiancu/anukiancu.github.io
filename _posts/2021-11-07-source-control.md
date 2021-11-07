---
layout: post
title: Shader Museum - Source Control
tags:
  - professional-practice
description: >
  
hero: /uploads/shader_museum_update.JPG
overlay: purple
published: true
---

# Source Control Is Essential
Over the past year or so I familiarised myself with Git, having used it for code and one Unity project. Being in my final year of univeristy, the last thing I'd want to happen is to lose my progress and have to start over. I initially tried to use it for my university work this year, and while it worked really well for my LOD tool, it didn't handle my Shader Museum too well.


# Git does not like binary files
I learned it the hard way. Whenever I'd push my work from uni and pull it from home, everything would work fine until I pushed from home and tried to work from uni again. Then, everything I had worked on was either completely broken or missing references, or missing altogether. I'm still trying to figure out why that was happening, as my project wasn't even over 2 GB then. 

So then, I figured I have two options: keep the project on **Git** and never work on it from home, but keep the source control functionality (rather than the "file sharing" side of it) or move my project to **Perforce**, not have the option to access my project from home through it, but have a good reliable form of source control that handles bigger projects much better. The latter sounded much better, as I would still be able to grab a zip of my project if I need it at home and inject the files I changed back into the project later on at university. Besides, Perforce is industry standard anyway, so this was a good opportunity to familiarise myself with it.

# Moving the Project to Perforce
Sounds easy in theory.. right? Wrong. Once more, technology was against me. No matter how hard I tried, Unreal would simply not let me select a Perforce Workspace. I thought it could be an issue with the SourceControl.ini files (UE4 very conveniently likes to create a bunch of these in different locations), as the project had been on git before, but that wasn't it.

Then I took troubleshooting a step further by trying to connect the same project to source control on a different computer. Surprisingly.. that worked. At least we know it's not the project that's causing the issue. So what is it then?

I thought it could be an issue with my User on my machine, so I tried to force a log out using Powershell. But Perforce kept remembering my credentials for some reason. But the mastermind that is our beloved IT support person came up with the idea of resetting my password, that ought to force me out of my Perforce account. And it worked! Well.. more or less. I then had a couple of issues trying to get the scene build data to save, as it kept saying it wasn't checked out from source control. 

It took some more fiddling around to finally get source control to work correctly, but nevertheless I am more than excited to head back to uni on Monday and have the peace of mind that nothing will get corrupted on git anymore. (famous last words)

### That's all from me now, I'm gonna go back to refreshing my grade 11 maths as a fun little exercise over a cup of tea. Aren't Sundays the best?

