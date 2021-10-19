# Boids_Boi
Trying to replicate (albeit unsuccessfully) the phenomenon of boids using Ursina (and VPython) in a naive manner.

Please install the Ursina module before running the code. More about that [here](https://www.ursinaengine.org/).

## This is an attempt to copy the simulation created by Ben Eater using Vanilla JavaScript

[Link to his code](https://github.com/beneater/boids) and to his amazing [simulation](https://eater.net/boids)

The premise for this simulation is the following (Please refer the above code too, where it has been explained in a much better way than I am going to here):
1. Each boid has to remain within some boundary. If it goes beyond a certain distance, the boid has to "turn" back.
2. There must be a speed limit, and if the boids reach this limit, then their speed must not increase beyond that.
3. If a boid comes really close to another, then it must be slightly" repelled away so that they don't collide.
4. Each boid has a visual range, and if there are other boids within this range, then the boid will move towards the centre of mass of the boids within it's visual range.
5. Also, the boid has to adjust it's speed so that it moves in almost the same speed as the other boids in it's visual range,

This is done in order to learn Ursina, and also probably create some new and interesting simulations.

- As of yet, the code is very inefficient, if the number of boids is increased beyond 20, then it starts getting choppy.
- Couldn't figure out a way to rotate the boids in their direction of motion. Need to work on that.

### At the beginning:
The boids are all separate here.
![Alt Text](https://github.com/ashish-kp/Boids_Boi/blob/main/pictures/Boids_1.png)

### After some time:
The boids have formed individual "flocks". As there are only 40 of them, and their sizes are small, they seem to be really close to each other. 
![Alt Text](https://github.com/ashish-kp/Boids_Boi/blob/main/pictures/Boids_2.png)

Here the number of boids is 40, so the fps is comparatively low. 

To do:
- Reduce complexity as the distance function is called almost 4*(number of boids)^2 times.
- Maybe attach an invisible sphere with a collider so that the computation load is reduced.  
- Also in Glowscript, to learn very basic raycasting or any form of collision detection to detect collisions and reduce complexity.

The same simulation using VPython [here](https://www.glowscript.org/#/user/p.b.ashish786/folder/MyPrograms/program/boids). Also added predator boids to it, from which the other boids move away from. The predators don't chase the boids, they just move like regular boids.

I've implemented a naive "predator boids" [here](https://www.glowscript.org/#/user/p.b.ashish786/folder/MyPrograms/program/boids2). The predators behave like normal boids and don't react to the boids, but the boids "fly away" from the predators.

It seems to be much more faster in VPython.

If viewing in a mobile, please use the Puffin Browser.
