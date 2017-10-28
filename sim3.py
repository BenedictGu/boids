import time
from world import world
from flock import flock
from leader import leader
from follower import follower
from geometry import point2d,vector2d

#
# CSCI 121: The Boids
# Project 3 Option #2 Exercise 3
# Fall 2017
#
# This script runs the simulation for EXERCISE 3.
#

# Initialize the world and its window.
w = world(60.0,45.0,800,600,topology='wrapped')

# Make the flock of follower birds and then add a leader.
f = flock(follower,25,w)
l = leader(point2d(0.0,0.0),vector2d(1.0,0.0),f,w)
f.add(l)
f.register_leader(l)

# Place all the flock's birds into the world.
w.add_system(f)

# Run the simulation indefinitely.
while True:
    time.sleep(0.01)
    w.step()
    w.render()
