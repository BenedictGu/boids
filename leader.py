from bird import bird
from geometry import vector2d

# EXERCISE 3
#
# . override 'color'
# . override 'steer' to pay attention to world.pointer(), if
#     the mouse pointer is far enough away.
#

class leader(bird):


    def color(self):
        return "#fff12d"


    def steer(self):
        vect_to_pointer = self.world.pointer() - self.position
        return vect_to_pointer.direction()

