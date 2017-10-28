from bird import bird
from geometry import vector2d, point2d


class herder(bird):

	#herder has a higher speed, so it can herd around the flock.
	MAXIMUM_SPEED = 1.5


	def color(self):
		return "#fff956"

	# steer:
	#
	# always head toward the right most insight
	def steer(self):
		f = []
		for b in self.flock:
			if type(b) != herder:
				f.append(b)
		h = self.position
		right_most = vector2d(-1,0)
		for b in f:
			b1 = b.position
			v1 = b1 - h
			if v1.cross(right_most) > 0:
				right_most = v1
		return right_most.direction()