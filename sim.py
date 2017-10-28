import time
from world import world
from flock import flock
from bird import bird

#
# CSCI 121: The Boids
# Project 3 Option #2
# Fall 2017
#
# This script runs a basic simulation to demonstrate the project.
# You'll mimic this script, write your own copy, for each of the
# exercises you choose to complete. (See sim1.py, sim2.py, etc.
# in this same folder for examples for their exercises.)
#

# Initialize the world and its window.
w = world(60.0,45.0,800,600,topology='wrapped')
w.add_system(flock(bird,25,w))

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    w.step()
    w.render()
