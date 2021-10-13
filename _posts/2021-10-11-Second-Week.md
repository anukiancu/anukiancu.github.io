---
layout: post
title: Second Week Progress and Goals 
tags:
  - professional-practice
description: >
  Example text
hero: /uploads/snowglobe.gif
overlay: purple
published: true
---
An overview of what I'm hoping to achieve during the second week of third year, as well as first week's progress.
{: .lead}


# Progress
I've made massive progress on both of my projects last week and I'm happy with the pace I'm working at right now. Doing both projects at once was a really good call, as whenever I get too tired of programming I can go into Unreal and play around with shaders, and the other way around.

## LOD Tool Progress
I've now added functionality for the tool to be able to output the number of LODs, the number of materials and the name of each mesh into a CSV file (an Excel file format). This was quite a big step, as it implied using multiple python libraries that I'm not particularly familiar with, but Google was my best friend.

We also had the great opportunity to have Malachi Duncan (technical artist @Epic Games) come in as a guest speaker last Friday, which was honestly a dream come true. I got to talk to an industry professional about my goals for each project and he gave me very valuable tips, like learning Houdini before I go into full time work. He also took one good look at my code and fixed a bug within 2 minutes. It was pretty mindblowing.


## Shader Museum Progress
Huge progress on this project last week. I made around 4 shaders, a snow one, an ice one, a northern lights one and a glass one. Other than that, I also made the snow particle system that I'll be using to create the interactive blueprint. I feel like moving forward, I should focus more on presentation, as I was told it matters just as much as your technical abilities. I have the layout of my museum in mind and I'm really excited to make it a real thing. 

I subconsciously set the theme for my museum to be Winter (or something like that), as all my shaders seem to have to do with the season. I really have no clue how that happened, but I'll go with it. I'm a huge Christmas person anyway.


![](/uploads/snowglobe.gif)




# Goals
My biggest goal for this week is to make the interactive snow globe blueprint. I want it to be able to generate snow when you walk up to it and press E. The snow should burst from one spawn location and fill up the entire globe, as well as be able to collide with the globe mesh. 

For a stretch goal, it would be cool for it to be able to alter the level of snow on the ground, so that when the snow falls the ground texture scales up on the Z axis. I think I know just how to do that with a reference to my Tesselation mask multiplier from my snow shader. 

![](/uploads/snow.jpg)

If I'm able to change this value from within the blueprint as the snow falls, that should be all I need to do.
