import time
from world import world
from flock import flock
from geometry import bounds
from bird import bird



# Initialize the world and its window.
wi = 60.0
h = 45.0
w = world(wi,h,800,600,topology='open')
f = flock(bird,25,w)
w.add_system(f)

for b in f:
	b.set_trail(True)

# Run the simulation indefinitely.
while True:
	time.sleep(0.01)
	#center the screen to a specific bird
	center = f.bodies[0].position
	w.bounds = bounds(center.x - wi/6, center.y - h/6,center.x + wi/6, center.y + h/6)
	w.step()
	w.render()