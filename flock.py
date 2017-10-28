from random import random
from geometry import point2d, vector2d
from bird import bird
from system import system

EPSILON = 0.000001

#
# flock.py
#
class flock(system):

    def __init__(self, cls, sz, wo):
        system.__init__(self,wo)
        self.leader   = None
        self.predator = None

        # Build the collection of birds.
        # Give each bird a random position and trajectory.
        for i in range(sz):
            p0 = point2d.random(self.world.bounds)
            v0 = vector2d.random(bird.MAXIMUM_SPEED)
            b = cls(p0, v0, self, self.world)
            self.add(b)

    def register_predator(self,p):
        self.predator = p

    def register_leader(self,l):
        self.leader = l

    
