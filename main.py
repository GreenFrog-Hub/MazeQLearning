import pyglet as pg
from pyglet.window import key
import cell, agent, random
from time import sleep
import Training

# Create a window  
window = pg.window.Window(width = 624, height = 624)

maze = ["WWWWWWWWWWWW",
        "W          W",
        "W          W",
        "W          W",
        "W          W",
        "W          W",
        "W          W",
        "W          W",
        "W          W",
        "W          W",
        "W         GW",
        "WWWWWWWWWWWW",]
tileArray=[]
for i in range(0,len(maze)):
        for j in range(0,len(maze[i])):
            tileArray.append(cell.cell(maze[i][j],j,i))

lermin = agent.Agent(grid=maze)

QLearn = Training.train(10000, tileArray)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.D:
        lermin.moveRight()
    elif symbol == key.A:
        lermin.moveLeft()
    elif symbol == key.W:
        lermin.moveUp()
    elif symbol == key.S:
        lermin.moveDown()
    elif symbol == key.Q:
        QLearn.printQTable()
        

def draw(dt):
    window.clear()
    for i in tileArray:
        i.update()
    action = 0
    action = QLearn.chooseAction(lermin.getPos())
    if action == 1:
        lermin.moveRight()
    elif action == 2:
        lermin.moveLeft()
    elif action == 3:
        lermin.moveUp()
    elif action == 4:
        lermin.moveDown()
    elif action > 4:
        print("shit")
    if action != -1:
        QLearn.updateQTable(lermin.getPos())
    else:
        lermin.setPos(1,1)
        QLearn.nextEpisode()
    if tileArray[lermin.getPos()].cellType == "G":
        lermin.setPos(1,1)
    lermin.update()
    #sleep(0.1)
    

pg.clock.schedule_interval(draw, 1/1200)
pg.app.run()