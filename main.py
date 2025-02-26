import pyglet as pg
from pyglet.window import key
import cell, agent, random
from time import sleep
import Training

# Create a window  
window = pg.window.Window(width = 1040, height = 1040)

maze = ["WWWWWWWWWWWWWWWWWWWW",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                  W",
        "W                 GW",
        "WWWWWWWWWWWWWWWWWWWW",]

tileArray=[]
for i in range(0,len(maze)):
        for j in range(0,len(maze[i])):
            tileArray.append(cell.cell(maze[i][j],j,i))

start = False
@window.event
def on_mouse_press(x, y, button, modifiers):
    xCoord = int(x//52)
    yCoord = int((1040-y)//52)
    if maze[yCoord][xCoord] == " " and start == False:
        s = list(maze[yCoord])
        s[xCoord] = "O"
        maze[yCoord] = "".join(s)

        tileArray[yCoord*20 + xCoord] = cell.cell("O", xCoord, yCoord)

#lermin = agent.Agent(grid=maze)
lermins = []
for i in range(0,25):
    lermins.append(agent.Agent(grid=maze))

QLearn = Training.train(10000, tileArray)



@window.event
def on_key_press(symbol, modifiers):
    global start
    if symbol == key.Q:
        QLearn.printQTable()
    elif symbol == key.ENTER:
        start = True
        

def draw(dt):
    window.clear()
    for i in tileArray:
        i.update()
    if start:
        for i in range(0,len(lermins)):
            action = 0
            action = QLearn.chooseAction(lermins[i].getPos())
            if action == 1:
                lermins[i].moveRight()
            elif action == 2:
                lermins[i].moveLeft()
            elif action == 3:
                lermins[i].moveUp()
            elif action == 4:
                lermins[i].moveDown()
            elif action > 4:
                print("shit")
            if action != -1:
                QLearn.updateQTable(lermins[i].getPos())
            else:
                lermins[i].setPos(1,1)
                QLearn.nextEpisode()
            if tileArray[lermins[i].getPos()].cellType == "G":
                lermins[i].setPos(1,1)
            elif tileArray[lermins[i].getPos()].cellType == "O":
                lermins[i].setPos(1,1)
            lermins[i].update()

pg.clock.schedule_interval(draw, 1/1200)
pg.app.run()