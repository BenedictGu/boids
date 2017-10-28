import random
import math

#
# geometry.py
#
# CSCI 121: The Boids
# Project 3 Option #2
# Fall 2017
#
# This defines three classes that we use to track bodies that
# occupy the world of our Boid simulation. Bodies inhabit a 2-D
# world at a position, have a velocity (a heading and a speed),
# and they are compelled (by their behavior) to change their
# heading. They also live within the bounds of the world.
#
# We define the classes
#
#   point2d: for tracking a location of a body
#   vector2d: for tracking the velocity and acceleration of a body; 
#     also used to talk about positions of bodies relative to others
#   bounds: used to track a rectangular region in the world
#
# These are described more carefully in the project description.
# The key methods are the "arithmetic" operations we define for
# working with point2d and vector2d. They are the following:
#
#   p + v : a point that is at vector offset v from a point p
#   v + w : a vector that is a combination of vectors v and w
#   p - q : the vector offset that thakes you from point q to point p
#   -v : a vector in the opposite heading of vector v
#   v * s : a vector whose length is scaled up by the float factor s
#   v / s : a vector whose length is scaled down by the float factor s
#   v - w : vector difference (same as v + (-w))
#
# We also support:
#
#   v.magnitude() : the length of vector v
#   v.direction() : a unit-length vector in the direction of v
#   v.dot(w) : the dot product of v with w (see the description, a float)
#   v.cross(w) : the cross product (or turn) of v with w (a float)
#
# Finally, we have a 'bounds' class for operating on points within a 2-D
# rectangular region.
#

class point2d:

    @classmethod
    def random(cls, bounds):
        return bounds.point_at(random.random(),random.random())


    def __init__(self, xCoord=0.0, yCoord=0.0):
        self.x = xCoord
        self.y = yCoord


    def copy(self):
        return point2d(self.x, self.y)


    def plus(self, offset):
        assert(type(offset) == vector2d)
        return point2d(self.x+offset.dx, self.y+offset.dy)


    def minus(self, arg):
        if type(arg) == vector2d:
            offset = arg
            return point2d(self.x-offset.dx, self.y-offset.dy)
        elif type(arg) == point2d:
            other = arg
            return vector2d(self.x-other.x, self.y-other.y)
        else:
            assert(type(arg) == vector2d or type(arg) == point2d)


    def get(self,coord):
        assert(coord == 0 or coord == 1 or coord == 'x' or coord == 'y')
        if coord == 0 or coord == 'x':
            return self.x
        else:
            return self.y


    def to_string(self):
        return "<P X="+str(self.x)+", Y="+str(self.y)+">"


    __add__  = plus
    __sub__  = minus
    __str__  = to_string
    __repr__ = to_string
    __getitem__ = get


class vector2d:

    EPSILON = 0.000001

    @classmethod
    def random(cls,length = 1.0):
        angle = random.random() * 2 * math.pi
        return vector2d(math.cos(angle), math.sin(angle)) * length


    def __init__(self, xOffset=0.0, yOffset=0.0):
        self.dx = xOffset
        self.dy = yOffset


    def perp(self):
        return vector2d(-self.dy, self.dx)


    def cross(self, vec):
        assert(type(vec) == vector2d)
        return self.dx*vec.dy - self.dy*vec.dx
    

    def dot(self, vec):
        assert(type(vec) == vector2d)
        return self.dx*vec.dx + self.dy*vec.dy
    

    def plus(self, vec):
        assert(type(vec) == vector2d)
        return vector2d(self.dx+vec.dx, self.dy+vec.dy)
    

    def minus(self, vec):
        assert(type(vec) == vector2d)
        return vector2d(self.dx-vec.dx, self.dy-vec.dy)
    

    def negated(self):
        return vector2d(0.0-self.dx, 0.0-self.dy)
    

    def times(self, amount):
        assert(type(amount) == float)
        return vector2d(amount*self.dx, amount*self.dy)
    

    def over(self, amount):
        assert(type(amount) == float)
        return vector2d(self.dx/amount, self.dy/amount)


    def magnitude(self):
        return math.sqrt(self.dot(self))


    def direction(self):
        mag = self.magnitude()
        if mag > vector2d.EPSILON:
            return self.over(mag)
        else:
            # return 0 vector if we are dividing by 0
            return vector2d()


    def to_string(self):
        return "<V DX="+str(self.dx)+", DY="+str(self.dy)+">"
    
    __add__ = plus
    __sub__ = minus
    __neg__ = negated
    __mul__ = times
    __rmul__ = times
    __truediv__ = over
    x = cross
    __str__ = to_string
    __repr__ = to_string


class bounds:

    def __init__(self,x0,y0,x1,y1):
        self.xmin = min(x0,x1)        
        self.xmax = max(x0,x1)
        self.ymin = min(y0,y1)        
        self.ymax = max(y0,y1)

    def width(self):
        return self.xmax - self.xmin

    def height(self):
        return self.ymax - self.ymin

    def point_at(self,fractionx,fractiony):
        x = self.xmin + fractionx * self.width()
        y = self.ymin + fractiony * self.height()
        return point2d(x,y)

    def wrap(self,position):
        p = position.copy()
        while p.x >= self.xmax:
            p.x -= self.width()
        while p.x < self.xmin:
            p.x += self.width()
        while p.y >= self.ymax:
            p.y -= self.height()
        while p.y < self.ymin:
            p.y += self.height()
        return p

    def clip(self,position):
        p = position.copy()
        if p.x >= self.xmax:
            p.x = self.xmax
        if p.x < self.xmin:
            p.x = self.xmin
        while p.y >= self.ymax:
            p.y = self.ymax
        while p.y < self.ymin:
            p.y = self.ymin
        return p
        
