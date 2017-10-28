import time
from geometry import vector2d, point2d
from world import world
from fireworks import fireworks



#iniate the world
w = world(60.0,45.0,800,600,topology='open')
f = fireworks(point2d(0, -21), vector2d(0,1), 30, True, w)
w.add_body(f)

# run the simulation
while True:
	time.sleep(0.01)
	w.step()
	w.render()