import time
from geometry import point2d, vector2d
from world import world
from flock import flock
from herder import herder
from bird import bird

#
# CSCI 121: The Boids
# Project 3 Option #2 Exercise 5
# Fall 2017
#
# This script runs the simulation for EXERCISE 5.
#


# Initialize the world and its window.
w = world(60.0,45.0,800,600,topology='wrapped')
f = flock(bird,16,w)
for _ in range(5):
    h = herder(point2d.random(w.bounds),vector2d(0.0,1.0),f,w)
    f.add(h)
w.add_system(f)

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    w.step()
    w.render()
