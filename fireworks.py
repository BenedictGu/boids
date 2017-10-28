from body import body
from trail import trail
from geometry import vector2d, point2d
import math


EPSILON = 0.000001


class fireworks(body):

	def __init__(self, p0, v0, lftm, b, wo):
		body.__init__(self, p0, v0, wo)
		self.age = 0
		self.lifetime = lftm
		self.burst = b

	# steer
	#
	# constant deceleration 
	def steer(self):
		return vector2d(0, -0.02)

	def color(self):
		return "#F7E7CE"

	def shape(self):
        # A little square is our generic shape.
		p1 = self.position + vector2d( 0.6, 0.6)       
		p2 = self.position + vector2d(-0.6, 0.6)        
		p3 = self.position + vector2d(-0.6,-0.6)        
		p4 = self.position + vector2d( 0.6,-0.6)
		return [p1,p2,p3,p4]

	# step:
	#
	# if the fireworks falls out of the window, remove the fireworks
	# if the speed of the fireworks reaches zero, burst out into several smaller fireworks.
	# But this process only undergoes once.
	# 
	def step(self, dt):
		if self.position.y < -25:
			self.world.remove_body(self)
		body.step(self, dt)
		self.age += 1
		t = trail(self.position, 12, self.world)
		self.world.add_body(t)
		if self.burst and self.velocity.magnitude() < EPSILON:
			bursts = []
			for n in range(1, 21):
				angle = 2*math.pi / 20 * n
				bursts.append(fireworks(self.position, vector2d(0.8*math.cos(angle), 0.8*math.sin(angle)), 10, False, self.world))
			for b in bursts:
				self.world.add_body(b)
			self.burst = False


