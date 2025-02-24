import pyglet as pg
from pyglet.window import key
import cell, agent, random
from time import sleep
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

player = agent.Agent(grid=maze)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.D:
        player.moveRight()
    elif symbol == key.A:
        player.moveLeft()
    elif symbol == key.W:
        player.moveUp()
    elif symbol == key.S:
        player.moveDown()
        

def draw(dt):
    window.clear()
    for i in tileArray:
        i.update()
    randNumb = random.randint(0,3)
    if randNumb == 0:
        player.moveRight()
    elif randNumb == 1:
        player.moveLeft()
    elif randNumb == 2:
        player.moveUp()
    elif randNumb == 3:
        player.moveDown()
    if tileArray[player.getPos()].cellType == "G":
        player.setPos(1,1)
    player.update()
    #sleep(0.1)
    

pg.clock.schedule_interval(draw, 1/60)
pg.app.run()