import time
from world import world
from flock import flock
from chaser import chaser
from mouse import mouse


w = world(60.0,45.0,800,600,topology='wrapped')

# Make the flock of chaser birds and place them into the world.
f = flock(chaser,25,w)
w.add_system(f)

# Make a mouse body and place it in the world.
m = mouse(w)
w.add_body(m)

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    w.step()
    w.render()
