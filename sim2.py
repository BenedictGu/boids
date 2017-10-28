import time
from world import world
from flock import flock
from chaser import chaser
from mouse import mouse

#
# CSCI 121: The Boids
# Project 3 Option #2 Exercise 2
# Fall 2017
#
# This script runs the simulation for EXERCISE 2.
#

# Initialize the world and its window.
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
