from bird import bird
from geometry import vector2d



class leader(bird):


    def color(self):
        return "#fff12d"


    def steer(self):
        vect_to_pointer = self.world.pointer() - self.position
        return vect_to_pointer.direction()

