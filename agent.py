import pyglet as pg
import random

class Agent:
    def __init__(self, grid):
        self.gridPos = [1,1]
        self.grid = grid.copy()
        self.agentImage = pg.resource.image("agent.png")

        self.sprite = pg.sprite.Sprite(img=self.agentImage, x= self.gridPos[0]*52, y=572-(self.gridPos[1]*52))
        self.backgroundColour = pg.shapes.Rectangle(x= self.gridPos[0]*52, y=572-(self.gridPos[1]*52),width=52,height=52,color=(
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        ))
    
    def moveLeft(self):
        if self.gridPos[0] > 1:
            self.gridPos[0] -=1

    def moveRight(self):
        if self.gridPos[0] < 10:
            self.gridPos[0] +=1
    
    def moveDown(self):
        if self.gridPos[1] < 10:
            self.gridPos[1] +=1
            
    def moveUp(self):
        if self.gridPos[1] > 1:
            self.gridPos[1] -=1

    def setPos(self, x, y):
        self.gridPos[0] = x
        self.gridPos[1] = y
    
    def getPos(self):
        return self.gridPos[0]+self.gridPos[1]*12
    
    def update(self):
        self.sprite.x = self.gridPos[0]*52
        self.backgroundColour.x = self.gridPos[0]*52
        self.sprite.y = 572-(self.gridPos[1]*52)
        self.backgroundColour.y = 572-(self.gridPos[1]*52)
        self.backgroundColour.draw()
        self.sprite.draw()