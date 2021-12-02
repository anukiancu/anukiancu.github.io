---
layout: post
title: Quick Projects Update
tags:
  - professional-practice
  - projects
description: >
  
hero: /uploads/code.JPG
overlay: purple
published: true
---
I thought it would be time to give a proper update on all the projects I have going on at the moment.

# Shader Museum
Although this project is basically finished, there's a bit of cleaning up to do in terms of all the shader iterations, and perhaps some optimisation to the shaders themselves. I decided to put this project on stand-by for a while and re-visit it after a couple of weeks, but then I remembered I wanted to animate some footsteps on top of the settled snow display.

The way I did that is by controlling the opacity of a decal using a material parameter collection scalar within a blueprint. Very quick and easy way to get this effect, but I'm sure this could be achieved in other ways as well.

Here's how I set up the material and the blueprint:

![](/uploads/snow_footstep_mat.JPG)
![](/uploads/snow_footstep_BP.JPG)

And here it is in action:

<video autoplay loop muted playsinline>
  <source src="/uploads/snow_footstep_decal1.mp4" type="video/mp4">
</video>

# Zen Room
After careful consideration and a bit of research, I decided that my handmade `Motion 4 Way` was a bit overkill, so insted I made a so called `Motion 2 Way`instead. It does exactly what it says on the tin, it creates the same sort of effect but only using the texture twice. I offset them both by (0, 0.5) and (0.5, 0) respectively, and made sure that they're panning in opposite directions, and vois-la:

<video autoplay loop muted playsinline>
  <source src="/uploads/motion-2-way.mp4" type="video/mp4">
</video>

![](/uploads/motion-2-way.JPG)

Now, I've finally started implementing the water mechanics, but they're not really behaving the way I need them to just yet. I'll definitely come back and update once they're fully functional!

# 1950's Diner
I haven't really made much progress on this one as I wanted a bit of a change of scenery (hence the Zen Room), but I will most certainly go back to it after I've implemented water mechanics in my other project. 

# LOD tool
Haven't touched this project in ages, but I still need to flatten some dictionaries for better data output; speaking of, I really need to figure out a way to output all my data to a log within a tool rather than the output log, so on the to-do list that goes!

### That's about it! If you'd like to see what I come up with next please keep an eye on here, hope you have a lovely day and take care! :)
