---
layout: post
title: Shader Museum - Shader Creation Process
tags:
  - professional-practice
description: >
  Example text
hero: /uploads//uploads/snowglobe.gif
overlay: purple
published: true
---

## Coming Up With the Idea
Creating a good shader implies a lot of research - from  the type of material to its surface properties, the process definitely isn't simple. But once you've got a general idea of what it is you want to make, it goes a lot more smoothly.

## The Shader Creation Process
The most essential part of my shader creation process is **iteration**. Whenever I get to a point where I like the way a shader behaves, I'll make a copy and continue experimenting from there, and so on and so forth. And just like that I end up with 15 material copies and 10000 material instances, but cleaning that up is a job for later.

### Ice
I started with a Ice material based on a stylised ice reference I found online. The shader uses tesselation and world displacement to create an icicle effect, so I ended up attempting to make sime from it too. That didn't quite work out, as I couldn't find the right noise to use for the displacement, and no matter what I did it looked really spikey. I will eventually go back to it and figure it out, but for now I realised it doesn't go with the general theme of my museum which is Winter.
### Snow
Then, still from the ice, I made snow, by changing the subsurface colour from blue to a light gray, and  adding parameters to change the U and V tilings of the normal maps, as well as a flatten normal node.

From there I experimented a lot with an emissive shimmering glitter system I set up like so:

![]()

The inspiration came from [this](https://www.artstation.com/blogs/ninaklos/la87/shader-museum-part-1-planning-sand-glitter) blog post, courtesy of Nina Klos. I decided to attempt to make my own version of the glitter effect she did for her sand shader, except my one was supposed to replicate the way snow glows in the light.

### Northern Lights
At this point it was very clear that the theme of my museum is Winter or Christmas or North Pole or just something to do with the cold season. Like I mentioned in a previous post, this all happened involuntarily, but I definitely don't mind.

I then figured that I should just think about everything that makes me think of this theme. Since I'm going to Norway this winter, I thought I could make that the focus of my project. Well then, what does Norway have that other countries don't have? **Northern lights**. And reindeers, but I don't think that would make a good shader. Oh and good food.. **anyway**.

I set up the base Northern Lights shader in a very simple but effective manner, by using an opacity map and a gradient to control the colours. From there, I wanted to experiment with dynamically changing the emissiveness in a blueprint, but I had no idea how one would go about doing that. An hour of Kat and I frantically trying to figure it out later, I finally found the solution. **Making a parameter collection**. By doing that, then creating a scalar parameter named `Emissive_control`, I was able to modulate it's value based on a timeline in blueprints. The result looks like this:

![]()


## The Museum Layout
One of the most crucial parts of this project is presentation. Technical ability is definitely right up there with it, but if my scene looks bad, I'm never going to be able to showcase my shaders properly. I started looking into Ice Hotels for reference, and I thought that looked cool, but maybe an igloo would be better, as I could play around with the way the outside world affects the walls. 

I'm yet to figure out exactly what I want it to look like, but I think having a little hole at the top of the igloo that you could see the sky from (and therefore the northern lights) would be a really good way to present my work.

### More Updates Soon! Thanks for reading.