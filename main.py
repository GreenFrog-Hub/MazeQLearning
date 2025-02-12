import pyglet as pg
import cell
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
def draw(dt):
    window.clear()
    for i in tileArray:
        i.update()
    

pg.clock.schedule_interval(draw, 1/60)
pg.app.run()