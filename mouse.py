from body import body
from geometry import vector2d, point2d


class mouse(body):

    def __init__(self,wo):
        body.__init__(self, wo.pointer(), vector2d(), wo)


    def color(self):
        return "#faff00"


    def step(self,dt):
        self.position = self.world.pointer()

