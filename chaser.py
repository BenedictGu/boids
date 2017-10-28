from geometry import vector2d
from bird import bird

# EXERCISE 2
#
# . add a 'chaser' subclass of 'bird' 
# . make a 'chaser.compute_chase' method that pays attention to self.world.pointer()
# . override 'steer' to use 'compute_chase' instead of 'compute_cohere'
#

class chaser(bird):


    def compute_chase(self):
        mouse = self.world.pointer()
        chaser = self.position
        dist = mouse - chaser
        offset = dist / (dist.magnitude())
        return offset


    def steer(self):
        # Compute the directions of three competing concerns.
        repel = self.compute_avoid()
        align = self.compute_mimic()
        group = self.compute_chase()

        # Compute a weighted average of these concerns' directions.
        accel = vector2d()
        accel = accel + repel.direction() * self.AVOID_COEFF
        accel = accel + align.direction() * self.MIMIC_COEFF
        accel = accel + group.direction() * self.COHERE_COEFF
        total_weight = self.AVOID_COEFF + self.MIMIC_COEFF + self.COHERE_COEFF
        return accel.over(total_weight)

