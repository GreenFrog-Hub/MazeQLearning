import pyglet as pg

class cell:
    def __init__(self, cellType,x, y):
        self.cellType= cellType
        self.weight = 0.0
        if self.cellType == "W":
            self.colour = (125,125,125,255)
            self.weightLabel = pg.text.Label(text="",x=x*52+26,y=y*52+26, anchor_x="center", anchor_y="center", color=self.colour)
        elif self.cellType == "G":
            self.colour = (0,255,0,255)
            self.weightLabel = pg.text.Label(text=str(self.weight),anchor_x="center", anchor_y="center",x=x*52+26, y=572-(y*52)+26, color=(0,0,0,255), font_size=7)
        else:
            self.colour = (255,255,255,255)
            self.weightLabel = pg.text.Label(text=str(self.weight),anchor_x="center", anchor_y="center",x=x*52+26, y=572-(y*52)+26, color=(0,0,0,255), font_size=7)

        self.shape = pg.shapes.BorderedRectangle(x*52, 572-(y*52), 52, 52, 1, color=self.colour, border_color=(0,0,0,255))
        
        
    
    def update(self):
        self.shape.draw()
        self.weightLabel.draw()