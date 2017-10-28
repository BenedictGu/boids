import time
from world import world
from flock import flock
from mass import mass
from geometry import bounds


# Initialize the world and its window.
wi = 60.0
h = 45.0
w = world(60.0,45.0,800,600,topology='open')
f = flock(mass,25,w) #a flock of masses
w.add_system(f)

# Run the simulation
while True:
    time.sleep(0.01)
    center = w.center_of_mass()
    w.bounds = bounds(center.x - wi/2, center.y - h/2, center.x + wi/2, center.y + h/2) # the camera is fixiated on the center of mass of the world
    w.step()
    w.render()