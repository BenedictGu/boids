import time
from world import world
from flock import flock
from bird import bird


# Initialize the world and its window.
w = world(60.0,45.0,800,600,topology='wrapped')
f = flock(bird,25,w)
w.add_system(f)

# Turn on the flock's trails.
for b in f:
    b.set_trail(True)

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    w.step()
    w.render()
