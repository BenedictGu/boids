from bird import bird
from geometry import vector2d

# EXERCISE 3
#
# . add a 'follower' subclass of 'bird' 
# . override 'compute_cohere' so that it pays attention to a leader when 
#     the flock has a leader in it. Otherwise, it should instead use its
#     superclass's 'compute_cohere' to govern its behavior.
#

#
# follower.py
#
# CSCI 121: The Boids
# Project 3 Option #2 Exercise 3
# Fall 2017
#

class follower(bird):

    def compute_cohere(self):
    	leader = self.flock.leader
    	if leader != None:
    		cohere = leader.position - self.position
    		return cohere.direction()
    	else:
    		return bird.compute_cohere(self)

