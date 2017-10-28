from body import body
from geometry import vector2d, point2d

# EXERCISE 2
#
# . override '__init__' so that it takes fewer arguments than the one for 'body',
#     but uses that __init__ of body.
# . override 'color' so that you can see the mouse object in the world
# . override 'step' to set position based on self.world.pointer()
#

class mouse(body):

    def __init__(self,wo):
        body.__init__(self, wo.pointer(), vector2d(), wo)


    def color(self):
        return "#faff00"


    def step(self,dt):
        self.position = self.world.pointer()

