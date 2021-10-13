---
layout: post
title: Footprint System in Unreal Engine
tags:
  - professional-practice
description: >
  Example text
hero: /uploads/footstep_demo.png
overlay: purple
published: true
---

# The logic behind the system
Before starting working on the actual blueprints, I made a clear list of things that I'm gonna need to make it work:

- a footprint opacity map for each foot
- a footprint normal for each foot
- deferred decal materials for each foot using the `dbuffer translucent normal` blending mode
- blueprints for each feet that uses a decal component with the materials created before

# The process

## Textures and Materials

I went through a trial and error process trying to find the best footprint textures for the task. Here's some of the ones I tried.

![](/uploads/T_footstep_left.png)
![](/uploads/T_footstep_left2.png)

In the end I went with this one.

![](/uploads/T_footstep_left3.png)

Then I proceeded to set up the materials like so: 

![](/uploads/material_foot.png)

## Blueprints

The first blueprint I made is using a decal component that has the footstep material in the allocated spot. I made one for each foot.

![](/uploads/foot_blueprint.png)

Next up, inside the **ThridPersonCharacter blueprint**, I added two plane components (these are going to display our decal). I parented them to the character mesh (`CharacterMesh0`) by dragging them under it, and added parent sockets to each of them, `foot_l` for the left foot plane, `foot_r` for the right foot plane.

![](/uploads/tp_blueprint1.png)

After that, I headed over to **Mannequin>Animations>ThirdPersonRun** to set a couple notifies when the foot touches the ground in the animation. I'm going to use these later on in the **ThirdPersonAnimation blueprint**.

![](/uploads/notify.png)


I can now go back to my **ThirdPersonCharacter blueprint** event graph to set up a couple custom events. I start by making a `SpawnFootprintL` event that spawns an actor from my `BP_Left_Footprint` (the decal component blueprint that contains the material). I then drag and drop a reference to my `Foot L plane` that I set up at the base of my character's foot, in order to be able to track its location. 

Initially, I thought the rotation of the footprint should be that of the plane, but thanks to [this](https://www.youtube.com/watch?v=8AZWZ1xaA78) tutorial I found out that it should actually just be the actor rotation.

I then went ahead and copy-pasted the code from the left foot and changed the reference and the class for the right foot (BP_Right_Footprint). 

![](/uploads/spawn_footprint.png)

Now that that's set up, I headed over to the **ThirdPersonAnimation blueprint** event graph. The logic here is that I want the footprints to spawn only when the feet touch the ground. I do that by getting an `Event Blueprint Begin Play` that's casted to the **ThirdPesonCharacter** and an `AnimNotify` event for each foot. What this will do is esentially, every time the animation notify I previously set up in the run animation is called, it will trigger the custom events I just set up inside the **ThirdPersonCharacter blueprint** and spawn a footstep.

![](/uploads/animation_bp.png)

Phew, that was a lot. Surprisingly, when I hit play, everything worked accordingly. All I needed to do now was to adjust the sizes of the decal blueprints to match the size of the player's foot. That took a bit of playing around, but in the end I got it to match pretty well.

![](/uploads/footprintdemo2.gif)

Hope you enjoyed my little (not so little) tutorial. It was a long process, but thankfully google is a thing nowadays.

### Resources I haven't previously mentioned:


[Normal map only footprints](https://answers.unrealengine.com/questions/398942/normal-map-only-footprints.html) - this is where I got the idea to use a DBuffer Decal blending mode instead of translucent.


[Unreal Engine 4 - Deforming Snow Tutorial](https://www.youtube.com/watch?v=rN4f-uVmYjc) - this was just general inspiration, I didn't end up doing this