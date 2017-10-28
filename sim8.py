import time
from world import world
from flock import flock
from bird import bird

#
# CSCI 121: The Boids
# Project 3 Option #2 Exercise 8
# Fall 2017
#
# This script runs the simulation for EXERCISE 8.
# Special avoiding pattern is added to compute_avoid in bird.py to avoid birds from a different flock

# Initialize the world and its window.
w = world(60.0,45.0,800,600,topology='wrapped')
f1 = flock(bird,12,w)
f2 = flock(bird,12,w)
w.add_system(f1)
w.add_system(f2)

# Turn on the flocks' trails.
for b in f1:
	b.set_trail(True)
	b.set_color("#C0C0C0")
for b in f2:
	b.set_trail(True)
	b.set_color("#0abab5")

# Run the simulation indefinitely.
while True:
	time.sleep(0.001)
	w.step()
	w.render()