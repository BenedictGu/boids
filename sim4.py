import time
from geometry import point2d, vector2d
from world import world
from flock import flock
from bird import bird
from hawk import hawk



# Initialize the world and its window.
w = world(60.0,45.0,800,600,topology='wrapped')
f = flock(bird,25,w)
w.add_system(f)
h = hawk(point2d(),vector2d(),f,w)
w.add_body(h)
f.register_predator(h)

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    w.step()
    w.render()
