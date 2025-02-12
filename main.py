import pyglet as pg
from pyglet.window import key
import cell, agent
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
    player.update()
    

pg.clock.schedule_interval(draw, 1/60)
pg.app.run()