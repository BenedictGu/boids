from bird import bird
from geometry import vector2d

#
# follower.py
#


class follower(bird):

    def compute_cohere(self):
    	leader = self.flock.leader
    	if leader != None:
    		cohere = leader.position - self.position
    		return cohere.direction()
    	else:
    		return bird.compute_cohere(self)

