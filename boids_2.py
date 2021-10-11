from ursina import *
import numpy as np

Boids = []
num = 50
ini_width = 10
ini_vel = 2
speed = 3
margin = 3
NudgeFactor = 2
sep_min = margin / 10
SeperationFactor = 1
VisualRange = margin / 5
CenteringFactor = 0.5
MatchingFactor = 0.4
max_speed = 2

def nudge(Ent):
	global margin
	global width
	global NudgeFactor
	if Ent.x > margin:
		Ent.vel[0] -= NudgeFactor * time.dt
	if Ent.x < -margin:
		Ent.vel[0] += NudgeFactor * time.dt
	if Ent.y > margin:
		Ent.vel[1] -= NudgeFactor * time.dt
	if Ent.y < -margin:
		Ent.vel[1] += NudgeFactor * time.dt
	if Ent.z > margin:
		Ent.vel[2] -= NudgeFactor * time.dt
	if Ent.z < -margin:
		Ent.vel[2] += NudgeFactor * time.dt

def distance(Ent1, Ent2):
	return np.linalg.norm(Ent1.position - Ent2.position)

def MoveAway(Ent):
	global Boids
	global sep_min
	global SeperationFactor
	move = Vec3(0, 0, 0) 
	for boi in Boids:
		if Ent != boi:
			if distance(Ent, boi) < sep_min:
				move = (Ent.position - boi.position) * SeperationFactor
	Ent.vel += move

def MoveTogether(Ent):
	global Boids
	global VisualRange
	global CenteringFactor
	c = Vec3(0, 0, 0)
	nN = 0
	for boid in Boids:
		if Ent != boid:
			if distance(Ent, boid) < VisualRange:
				c += boid.position
				nN += 1
	c /= nN
	if nN > 0:
		Ent.vel -= (Ent.position - c) * CenteringFactor

def MoveEqual(Ent):
	global Boids
	global MatchingFactor
	Avg = Vec3(0, 0, 0)
	nN = 0
	for boid in Boids:
		if distance(Ent, boid) < VisualRange:
			if Ent != boid:
				Avg += boid.vel
				nN += 1
	if nN > 0:
		Avg /= nN
		Ent.vel += (Avg - Ent.vel) * MatchingFactor

def MoveSlow(Ent):
	global max_speed 
	speed = np.linalg.norm(Ent.vel)
	if speed > max_speed:
		Ent.vel *= (max_speed / speed) 

def update():
	global speed
	for boid in Boids:
		nudge(boid)
		MoveAway(boid)
		MoveTogether(boid)
		MoveEqual(boid)
		MoveSlow(boid)
		boid.rotation = boid.vel * 90
		boid.position += boid.vel * time.dt * speed
		

app = Ursina()
for i in range(num):
	if i == 0:
		col = color.red
	else:
		col = color.white
	pos = Vec3((np.random.random() * ini_width) - (ini_width / 2), (np.random.random() * ini_width) - (ini_width / 2), (np.random.random() * ini_width) - (ini_width / 2))
	c = Entity(model = "diamond", position = pos, scale = (0.4, 0.2, 0.2), texture = "brick", color = col)
	c.vel = Vec3((np.random.random() * ini_vel) - (ini_vel / 2), (np.random.random() * ini_vel) - (ini_vel / 2), (np.random.random() * ini_vel) - (ini_vel / 2))
	c.acc = Vec3(0, 0, 0)
	Boids.append(c)
camera.z = -60
EditorCamera()
app.run()