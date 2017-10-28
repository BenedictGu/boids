from body import body
from geometry import vector2d

# EXERCISE 1
#
# . complete __init__ so it sets self.age and self.lifetime
# . override 'step' so that it instead:
#      . increases self.age
#      . removes itself from self.world if lifetime has been exceeded (using
#           the world's 'remove_body' method)
# . override the 'color' method. If you want, a nice effect is to have the
#     color vary with age.
#

class trail(body):

    def __init__(self,p0,lftm,wo):

        # call the superclass initializer
        body.__init__(self,p0,vector2d(),wo)

        # and then do more
        self.age = 0
        self.lifetime = lftm


    def color(self):
        # return a color code (see body.py and bird.py for examples)
        stri = "#" + "FF" + hex(int(73 + (206 - 73) * self.age / self.lifetime))[-2:] + hex(int(125 + (220 - 125) * self.age / self.lifetime))[-2:]
        return stri


    def step(self,dt):
        self.age += 1
        if self.age > self.lifetime:
            self.world.remove_body(self)
