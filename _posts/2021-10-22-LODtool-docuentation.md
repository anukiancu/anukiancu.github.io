---
layout: post
title: LOD tool - How to Use It 
tags:
  - professional-practice
description: >
  Example text
hero: /uploads/code.JPG
overlay: purple
published: true
---

# The Finished Product

I'm not going to lie, I'm kind of sad that this project is over. I had so much fun making this tool and it was so rewarding to see it work as intended, nothing quite compares to that feeling. Sure shaders are fun and all, but I really enjoyed the process of troubleshooting my code for ages and then finally realising what's wrong with it. I feel like I've learned so much during this project, from python syntax to how to use an API and make a UI for a tool in Unreal Engine 4. 

Anyway, enough talk, let's get into how to actually use the LOD Validating Tool.

# The Step by Step Guide
## The Output Log
The LOD Validating Tool uses UE4's built in `Output Log` to display data to its user. Opening it should be as easy as navigating to `Window>Developer Tools>Output Log`. Make sure you `right click>Clear Log` before you run the tool, in order to see its output more clearly.

## Opening the UI
The tool is located in the `Scripts` folder (within the Shader Museum project), and it is named `WBP_LODtool`. To run it, you need to right click it and select the first option at the top, `Run Editor Utility Widget`. This will then open this UI. 

![](/uploads/UI2.JPG)

## Using the Tool
In order to run the LOD Validating Tool and get an output, you first need to select a **Static Mesh** in the content browser. With it selected, you can then press any buttons on the tool's UI and it should output all the information about the mesh in the `Output Log`. 

##  Okay but what do the buttons do?
I named each button so that what pressing it does is self explanatory, but just to be sure I'll document that on here as well.
### Asset Operations:
- `Get Mesh Name` will output **the name of the mesh(es)** you slected in the content browser
- `Get Bounding Diameter` will give you **the diameter of the bounding sphere** of the mesh(es)
### LOD Operations:
- `Get Number of LODs` shows **the number of LODs** currently present on the mesh(es)
- `Get Number of Materials` gives you **the number of materials** on the mesh(es)
- `Get Number of Triangles for each LOD` outputs **the LOD indexes and the number of triangles they have**
- `Get LOD Screen Sizes` will give you **the screen sizes of the LODs** on the mesh(es)
- `Get LOD Vertex Density` outputs **the vertex density for each LOD** on the mesh(es), calculated by dividing the number of vertices by the bounding diameter of the LOD
- `Get Number of LOD UV Channels` shows **the number of UV channels present on each LOD** of the mesh(es)
- `Get Vertex Colours` outputs **True/False** depending on whether the LOD has Vertex Colours or not
- `Create Excel Report` will gather **all the data from above** and export it as a `.csv` file in the same directory as the .uproject file
- `Remove LODs` **removes all the LODs** present on the mesh(es)

That's about it! I tried to make the tool easy to use by providing a simple and intuitive UI. Throughout the next week, I will ask people if they want to try it out in their projects and see how easy it is for them to figure out the functionality, and based on that I might tweak the UI. 

### Thank you for reading!
