from tkinter import *
from system import system
from geometry import bounds, point2d

#
# world.py
#

class world(Frame):

    def __init__(self, w, h, ww, wh, topology = 'wrapped'):

        # Register the world coordinate and graphics parameters.
        self.WINDOW_WIDTH = ww
        self.WINDOW_HEIGHT = wh
        self.bounds = bounds(-w/2,-h/2,w/2,h/2)
        self.topology = topology

        # Populate the world with creatures
        self.bodies = system(self)

        # Initialize the graphics window.
        self.root = Tk()
        self.root.title('MATH 121 Bird Simulation')
        Frame.__init__(self, self.root)
        self.canvas = Canvas(self.root, 
                             width=self.WINDOW_WIDTH,
                             height=self.WINDOW_HEIGHT)

        # Handle mouse pointer motion events.
        self.mouse = point2d()
        def motion(event):
            self.mouse = self.window_to_world(event.x,event.y)
        self.canvas.bind('<Motion>',motion)

        # Finalize the creation of the windowed display.
        self.canvas.pack()
        self.pack()
        self.render()


    def trim(self,bdy):
        if self.topology == 'wrapped':
            bdy.position = self.bounds.wrap(bdy.position)
        elif self.topology == 'bound':
            bdy.position = self.bounds.clip(bdy.position)
        elif self.topology == 'open':
            pass

    
    def step(self):
        # A step of 0.5 was chosen judiciously.
        self.bodies.step(0.5)

    
    def add_body(self, bdy):
        self.bodies.add(bdy)


    
    def remove_body(self, bdy):
        self.bodies.remove(bdy)


    
    def add_system(self, syst):
        for bdy in syst:
            self.add_body(bdy)
               
    
    def render(self):
        self.clear()
        for bdy in self.bodies:
            shape = bdy.shape()
            color = bdy.color()
            self.draw_shape(shape,color)
        self.update()


    def draw_shape(self, shape, color):

        wh = self.WINDOW_HEIGHT
        h = self.bounds.height()
        ww = self.WINDOW_WIDTH
        x = self.bounds.xmin
        y = self.bounds.ymin
        pairs = [ ((p.x - x)*wh/h, wh - (p.y - y)* wh/h) for p in shape ]
        pairs.append(pairs[0])
        self.canvas.create_polygon(pairs, fill=color)

    
    def clear(self):
        self.canvas.delete('all')
        self.canvas.create_rectangle(0, 
                                     0, 
                                     self.WINDOW_WIDTH, 
                                     self.WINDOW_HEIGHT,
                                     fill="#000000")


    def window_to_world(self,x,y):
        return self.bounds.point_at(x/self.WINDOW_WIDTH,
                                    1.0-y/self.WINDOW_HEIGHT)


    def pointer(self):
        return self.mouse.copy()


        
    #center_of_mass:
    #
    # Calculate the center of all masses of a world instance
    #
    def center_of_mass(self):
        bodies = self.bodies
        x = 0
        y = 0
        count = 0
        for m in bodies:
            x += m.position.x
            y += m.position.y
            count += 1
        return point2d(x/count,y/count)
