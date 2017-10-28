from geometry import vector2d

#
# body.py
#

class body:

    def __init__(self, p0, v0, wo):
        self.position0 = p0
        self.velocity0 = v0
        self.world = wo
        self.reset()


    def reset(self):
        self.position = self.position0
        self.velocity = self.velocity0
        self.accel = vector2d()


    def color(self):
        # Blue is the default color.
        return "#000080"


    def shape(self):
        # A little square is our generic shape.
        p1 = self.position + vector2d( 0.125, 0.125)       
        p2 = self.position + vector2d(-0.125, 0.125)        
        p3 = self.position + vector2d(-0.125,-0.125)        
        p4 = self.position + vector2d( 0.125,-0.125)
        return [p1,p2,p3,p4]


    def steer(self):
        # By default, bodies don't move.  Return the 0 vector.
        return vector2d()


    # step
    #
    # This computes the boid's physical parameters in the next time step.
    #
    def step(self, dt):

        # Determine direction boid would like to head.
        self.position = self.position + self.velocity * dt
        self.velocity = self.velocity + self.accel * dt
        self.accel = self.steer()

        # Make sure that the quantities are limited appropriately.
        self.trim_physics()
    

    def trim_physics(self):
        # By default, make sure the coordinates of the position 
        # of the body respect the world's topology.
        self.world.trim(self)
