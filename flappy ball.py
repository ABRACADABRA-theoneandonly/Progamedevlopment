import pgzrun
WIDTH=600
HEIGHT=500
class Flappy():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.vx=200
        self.vy=0
        self.radius=25
    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,"yellow")
Bird=Flappy(50,250)
def draw():
    screen.clear()
    screen.fill("light blue")
    Bird.draw()
pgzrun.go()