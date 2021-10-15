GlowScript 3.1 VPython

boids = []
predators = []

r = 0.2
l = 0.6
n = 100 # Number of boids
p = 3 # Number of predators
max_speed = 5
margin = 5
NudgeFactor = 1
seperationFactor = 0.5
seperationDistance = 2
Cohesiondist = 3
Cohesionfactor = 0.1
MatchingFactor = 0.1
FearDistance = 5
FearFactor = 1

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

def run_away(Ent):
    nn = 0
    dista = vec(0, 0, 0)
    for pred in predators:
        if dist(pred, Ent) < FearDistance:
            dista += pred.pos
            nn += 1
    if nn > 0:
        dista /= nn
        Ent.vel -= (dista - Ent.pos) * FearFactor
        
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
    
for j in range(p):                                    # Comment this entire loop if u don't want predators
    position = position = vec((random() * margin) - (margin / 2), (random() * margin) - (margin / 2), (random() * margin) - (margin / 2))
    axis_b = vec((random() * 2 * pi)- pi, (random() * 2 * pi) - pi, (random() * 2 * pi) - pi)
    predators.append((cone(radius = 3 * r, length = 3 * l, pos = position, axis = axis_b, color = color.red, vel = axis_b)))
    
scene.camera.pos = vec(0, 0, 15)
 
dt = 0.1

while True:
    rate(300)
#    print(scene.mouse.pos)
    for boid in boids:
        Nudge(boid)
        maxspeed(boid)
        move_together(boid)
        move_away(boid)
        move_equal(boid)
        run_away(boid)                               # Comment this line if u don't want predators.
        boid.axis = l * hat(boid.vel)
        boid.pos += boid.vel * dt
    for pred in predators:                           # Comment this for loop if u don't want predators.
        Nudge(pred)
        maxspeed(pred)
        move_away(pred)
        move_equal(pred)
        move_together(pred)
        pred.axis = 3 * l * hat(pred.vel)
        pred.pos += pred.vel * dt
    
