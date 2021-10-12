GlowScript 3.1 VPython

boids = []

r = 0.2
l = 0.6
n = 50
max_speed = 5
margin = 10
NudgeFactor = 0.5
seperationFactor = 1
seperationDistance = 2
Cohesiondist = 3
Cohesionfactor = 0.1
MatchingFactor = 0.1

def Nudge(Ent):
    if Ent.pos.x > margin:
        Ent.vel.x -= NudgeFactor
    if Ent.pos.x < -margin:
        Ent.vel.x += NudgeFactor
    if Ent.pos.y > margin:
        Ent.vel.y -= NudgeFactor
    if Ent.pos.y <- margin:
        Ent.vel.y += NudgeFactor
    if Ent.pos.z > margin:
        Ent.vel.z -= NudgeFactor
    if Ent.pos.z < -margin:
        Ent.vel.z += NudgeFactor
        
def maxspeed(Ent):
    if mag(Ent.vel) > max_speed:
        Ent.vel = hat(Ent.vel) * max_speed
        
def dist(Ent1, Ent2):
    return mag(Ent1.pos - Ent2.pos)
    
def move_together(Ent1):
    avg = vec(0, 0, 0)
    nn = 0
    for Ent2 in boids:
        if Ent2 != Ent1:
            if dist(Ent1, Ent2) < Cohesiondist:
                nn += 1
                avg += Ent2.pos
    if nn > 0:
        avg /= nn
        Ent1.vel += (avg - Ent1.pos) * Cohesionfactor
    
def move_away(Ent1):
    nn = 0
    dista = vec(0, 0, 0)
    for Ent2 in boids:
        if Ent2 != Ent1:
            if dist(Ent1, Ent2) < seperationDistance:
                dista += Ent2.pos
                nn += 1
    if nn > 0:
        dista /= nn
        Ent1.vel -= (dista - Ent1.pos) * seperationFactor
        
def move_equal(Ent1):
    nn = 0
    avg = vec(0, 0, 0)
    for Ent2 in boids:
        if Ent2 != Ent1:
            if dist(Ent2, Ent1) < Cohesiondist:
                nn += 1
                avg += Ent2.vel
    if nn > 0:
        avg /= nn
        Ent1.vel += avg * MatchingFactor

for i in range(n):
    position = vec((random() * margin) - (margin / 2), (random() * margin) - (margin / 2), (random() * margin) - (margin / 2))
    axis_b = vec((random() * 2 * pi)- pi, (random() * 2 * pi) - pi, (random() * 2 * pi) - pi)
    boids.append(cone(radius = r, length = l, pos = position, axis = axis_b, vel = axis_b.hat * 2, acc = hat(axis_b) * random(), vel = axis_b))
    
#scene.camera.pos = vec(0, 0, 100)
 
dt = 0.01

while True:
    rate(300)
    for boid in boids:
        Nudge(boid)
        maxspeed(boid)
        move_together(boid)
        move_away(boid)
        boid.axis = l * hat(boid.vel)
        boid.pos += boid.vel * dt
    
