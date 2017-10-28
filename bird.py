from body import body
from trail import trail
from geometry import vector2d, point2d

#
# bird.py
#
# CSCI 121: The Boids
# Project 3 Option #2
# Fall 2017
#
# This defines the 'bird' class, a simulated body that moves in a
# world according to its behavior, determined by its own motivations
# and the presence of other bodies it reacts to.
#
# Below are the modifications we suggest for each of the exercises.
#

# EXERCISE 1
#
# . add a 'leave_trail' attribute that is either True/False
# . add a 'def set_trail(b)' method where 'b' is either True/False, for
#     turning on/off a bird's trail-leaving feature
# . modify 'step' to create a trail object body at a bird's position, but
#     only when it should be leaving a trail
#

# EXERCISE 4
#
# . create a FLEE_COEFF (and perhaps a FLEE_RADIUS)
# . make compute_flee compute acceleration component when
#     there's a predator (nearby, according to FLEE_RADIUS)
# . change steer to compute_flee using FLEE_COEFF
# . set the 'worried' attribute to True when it sees a predator,
#     otherwise have that attribute be False
#

EPSILON = 0.000001

#
# class bird
#
# Implements one of the flocking agents, one of Reynolds' "boids".
# A bird has a velocity and a position.  These get updated over
# time using first-order Euler integration.  This is handled in
# the method "step", which relies on the point2d and vector2d
# methods to modify a bird's position according to its velocity.
#
class bird(body):

    MAXIMUM_SPEED = 1.0
    AGILITY = 1.0
    AVOID_RADIUS = 5.0
    MIMIC_RADIUS = 10.0
    COHERE_RADIUS = 20.0
    AVOID_COEFF = 10.0
    MIMIC_COEFF = 10.0
    COHERE_COEFF = 5.0
    FLEE_COEFF = 15.0
    FLEE_RADIUS = 10.0




    def __init__(self, p0, v0, fl, wo):
        self.flock = fl
        self.worried = False
        self.leave_trail = False
        body.__init__(self,p0,v0,wo)

    def set_trail(self, b):
        self.leave_trail = b

    def set_color(self, c):
        assert(type(c) == str)
        self.color = lambda : c

    def color(self):
        # These birds are white, unless they are flustered.
        if self.worried:
            return "#FF8080"
        else:
            return "#FFFFFF"


    def shape(self):
        h = self.velocity.direction()
        hp = h.perp()
        p1 = self.position + h
        p2 = self.position + hp * 0.5
        p3 = self.position - hp * 0.5
        return [p1,p2,p3]


    def trim_physics(self):
        # Trim the position.
        self.world.trim(self)

        # Limit the bird's speed.
        self.velocity = self.velocity.direction() * self.MAXIMUM_SPEED

        # Limit the change in heading.
        self.accel = self.accel.direction() * self.AGILITY


    def compute_cohere(self):

        # Try to be around other birds.
        cohere  = vector2d()
        concern = self.flock.within(self.COHERE_RADIUS, self)
        for other in concern:
            offset = other.position - self.position
            cohere = cohere + offset

        # We'll normalize this.  If we don't, birds will work harder if
        # they are further away from the center of the group.  That's
        # a nice effect, too.
        return cohere.direction()


    def compute_mimic(self):
        # Try to mimic the heading of nearby birds.
        align = vector2d()
        concern= self.flock.within(self.MIMIC_RADIUS, self)
        for other in concern:
            align = align + other.velocity
        return align.direction()


    def compute_avoid(self):
        # Try to avoid nearby birds.
        separate = vector2d()
        concern = self.flock.within(self.AVOID_RADIUS,self)
        for bird in concern:
            offset = bird.position - self.position
            distance = offset.magnitude()
            if distance > EPSILON:
                # Head away from this other bird, with a
                # strength proportional to 1/d^2.  Closer
                # birds should be avoided more furiously.
                away = -offset
                weight = 1.0 / distance * distance
                separate = separate + away * weight
        #calculate the accel for avoiding birds in another flock
        other = []
        #a list of birds in the other flocks
        for b in self.world.bodies:
            if type(b) == type(self) and b.flock is not self.flock:
                other.append(b)
        # calculate the center of the other flock
        x = 0.0
        y = 0.0
        for bi in other:
            x += bi.position.x
            y += bi.position.y
        other_pos = point2d(x,y)
        # divide the acceleration by weight
        v = self.position - other_pos
        dist = v.magnitude()
        separate += v / (dist * dist) * float(len(other)) * 3.0
        return separate


    def compute_flee(self):
        # Exercise 4
        if self.flock.predator != None:
            if (self.position - self.flock.predator.position).magnitude() < self.FLEE_RADIUS:
                self.worried = True
                accel = self.position - self.flock.predator.position
                return accel
            else:
                self.worried = False
        else:
            pass

    #
    # steer and/or apply thrust
    #
    # Figure out the acceleration direction of one bird
    # by having it compare itself to the others.
    #
    def steer(self):

        # Compute the directions of three competing concerns.
        repel = self.compute_avoid()
        align = self.compute_mimic()
        group = self.compute_cohere()
        flee = self.compute_flee()

        # Compute a weighted average of these concerns' directions.
        accel = vector2d()
        accel = accel + repel.direction() * self.AVOID_COEFF
        accel = accel + align.direction() * self.MIMIC_COEFF
        accel = accel + group.direction() * self.COHERE_COEFF
        if flee != None:
            accel += flee.direction() * self.FLEE_COEFF
        total_weight = self.AVOID_COEFF + self.MIMIC_COEFF + self.COHERE_COEFF + self.FLEE_COEFF
        return accel.over(total_weight)


    #
    # step
    #
    # Change position, etc with a time step.
    # also leaves trail if it is set up to do so.
    def step(self,dt):
        body.step(self,dt)
        if self.leave_trail:
            t = trail(self.position, 12, self.world)
            self.world.add_body(t)


    # __str__
    #
    # Gives a bird report, decribing its position.
    #
    def __str__(self):
        return "bird at "+str(self.position)
