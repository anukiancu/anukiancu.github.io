---
layout: post
title: Side Project - Asset Renaming Tool
tags:
  - professional-practice
description: >
  Example text
hero: /uploads/asset_renaming2.png
overlay: purple
published: true
---

# About the tool that makes everyone's lives easier
Over the course of the last few couple of weeks, I've been so into my LOD tool project, constantly learning and wanting to improve, that I felt like I needed to try doing something else with the unreal python API to further expand my knowledge and understanding of it. 
{: .lead}

So I chose to make a little tool that takes all the assets you've selected in the content browser, identifies whether they're a `material`, `texture` or `static mesh` and adds the prefix `M_`, `T_` or `SM_` to its name accordingly.

After making sure that everything works properly in my own projects, I decided it would be time to share it with my classmates and see what they think about it. The first two versions of this tool didn't have a UI, so it wasn't too intuitive to use, as you would have to run it from the `context menu`. Later on however, I decided to give it a simple interface and have people try it out again. The response has been much better ever since.

![](/uploads/asset_renaming.png)

Now, I realise a tool like this is nothing in the grand scheme of things and that most studios have probably had something like this for ages, but as a student and someone new to python, I think it was good practice.

You can download the `.uasset` file [here](https://drive.google.com/file/d/1iHUWlhPTWl8qukxdkDb1-GYiXAUA8qXb/view?usp=sharing). Feel free to use it in your project.

### Thanks for reading!