import time
from world import world
from flock import flock
from bird import bird


# Initialize the world and its window.
w = world(60.0,45.0,800,600,topology='wrapped')
w.add_system(flock(bird,25,w))

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    w.step()
    w.render()
