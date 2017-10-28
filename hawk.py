from bird import bird
from geometry import vector2d, point2d

EPSILON = 0.000001

class hawk(bird):
	FOCUS = 0.8

	MAXIMUM_SPEED = 0.9

	def color(self):
		return "#FF0000"

	def steer(self):
		birds = self.flock
		direction = vector2d()
		weight = EPSILON
		hd = self.velocity.direction()
		for b in birds:
			bd = b.velocity.direction()
			if ((b.velocity - self.velocity).direction()).dot(bd) > 0.8:
				weight = weight + 1
				direction = direction + bd
		direction = direction / weight
		return direction
