#
# system.py
#

class system:

    def __init__(self,wo):
        self.world = wo
        self.bodies = []


    # within
    #
    # Returns a list of bodies that are within a certain
    # radius of the given body.
    #
    def within(self,radius,body):
        bs = []
        for b in self.bodies:
            if b is not body and (b.position - body.position).magnitude() <= radius:
                bs.append(b)
        return bs


    # step
    #
    # Advances the system's simulation by one time step.
    #
    def step(self,dt):

        # Adjust each body's physical parameters.
        for b in self.bodies:
            b.step(dt)


    # add
    #
    # Adds a body to the system.
    #
    def add(self,bdy):
        self.bodies.append(bdy)


    # remove
    #
    # Removes a body from the system.
    #
    def remove(self,bdy):
        self.bodies.remove(bdy)


    #
    # Quick way to get "for b in sys:" to work.
    #
    def __getitem__(self,i):
        return self.bodies[i]
