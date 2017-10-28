from random import random
from geometry import point2d, vector2d
from bird import bird
from system import system

EPSILON = 0.000001

#
# flock.py
#
# CSCI 121: The Boids
# Project 3 Option #2
# Fall 2017
#

#
# DESCRIPTION:
#
# The code below keeps track of a flock of birds for a bird 
# simulation.  It inherits from class 'system'.
#
#   __init__ : construct a flock of birds of a specified subclass
#   register_leader: for EXERCISE 3
#   register_predator: for EXERCISE 4
#
class flock(system):

    # flock(cls,sz,wo):
    #
    # Create a new instance with 'sz' new birds, with each being
    # an instance of class 'cls'. These all get added to the 
    # world 'wo'.
    #
    def __init__(self, cls, sz, wo):
        system.__init__(self,wo)
        self.leader   = None
        self.predator = None

        # Build the collection of birds.
        # Give each bird a random position and trajectory.
        for i in range(sz):
            p0 = point2d.random(self.world.bounds)
            v0 = vector2d.random(bird.MAXIMUM_SPEED)
            # The provided class 'cls' better have a bird-like __init__.
            b = cls(p0, v0, self, self.world)
            self.add(b)

    def register_predator(self,p):
        self.predator = p

    def register_leader(self,l):
        self.leader = l

    
