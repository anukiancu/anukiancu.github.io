---
layout: post
title: Zen Room - Personal Project
tags:
  - professional-practice
  - projects
description: >
  
hero: /uploads/caustics_texture.PNG
overlay: purple
published: true
---

You may remember I was working on a 1950's diner project just about a week ago. Well, one morning I saw this photo on instagram and it immediately inspired me to wanna try doing something similar in Unreal Engine.

![](/uploads/caustics_inspo.png)

# Using Lights to Achieve Caustics
After gathering some reference, the idea was to use lights in order to get the effect of water caustics. Here's what that looked like:

<video autoplay loop muted playsinline>
  <source src="/uploads/caustics_lights.mp4" type="video/mp4">
</video>

![](/uploads/caustics_lights.PNG)

And this is how I set up the light function:

![](/uploads/caustics_light_functions.PNG)

However, during an interview I got asked what would be a more optimised way to get the same effect - and then I realised I should use a panning emissive texture instead on the walls and floor.

# Doing Things the Better Way
Even though the lights were giving me the result I wanted, any technical artist would've screamed if they saw 3 lights being used that way. Dodged a bullet there. 

Regardless, I initially set up the emissive texture the same way I set up the light function, using a `Motion 4 Way` node. Then I realised, during the same interview I got asked to delete that node and make it from scratch instead. That way I would get the result I wanted with as few instructions as possible, removing any bloat/functionality I didn't need.

Here's the new and improved effect:

<video autoplay loop muted playsinline>
  <source src="/uploads/caustics_texture.mp4" type="video/mp4">
</video>

![](/uploads/caustics_texture.PNG)

And how it's set up:

![](/uploads/caustics_handmade.PNG)

This scene has a grand total of one directional light at the moment. I'm quite happy with it, but I might increase the chromatic aberration on the texture a little bit.

# Project Goals
The biggest goal for this project is to get the water to move with the player, probably using render targets. I would also like to add some custom specularity to it, so that it reflects the light in a pretty way.

I will most definitely update as soon as I get either of the two working in engine. I've already learned a lot during this project and I've only really started working on in a couple days ago. I'm happy to be able to say that each day is like a school day, the learning never stops and that's what keeps tech art fun. 

I'm also glad I was able to get such valuable feedback during my interview, and put it to good use straight away. Constructive feedback is an important part of development and I feel like I realise it now more than ever.

Anyway, that's all for now, thank you so much for reading, take care and hope to see you on here again soon!