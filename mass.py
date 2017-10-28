from body import body
from geometry import vector2d, point2d


class mass(body):

	#a mass knows its flock
	def __init__(self, p0, v0, fl, wo):
		self.flock = fl
		body.__init__(self, p0, v0, wo)

	def shape(self):
		h = self.velocity.direction()
		hp = h.perp()
		p1 = self.position + h
		p2 = self.position + hp * 0.5
		p3 = self.position - hp * 0.5
		return [p1,p2,p3]

	def color(self):
		return "#FF8080"

	#steer
	#
	#a mass' accel is an accumulation of the effect from other masses on itself.
	def steer(self):
		f = self.flock.bodies
		accel = vector2d()
		for m in f:
			if m is not self:
				v = m.position - self.position
				accel += v / v.magnitude()**2
		return accel