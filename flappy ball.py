import pgzrun
WIDTH=600
HEIGHT=500
gravity=1500
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
def update(dt):
    uy=Bird.vy
    Bird.vy+=gravity*dt
    Bird.y+=(uy+Bird.vy)*0.5*dt
    if Bird.y > HEIGHT-Bird.radius:
        Bird.y=HEIGHT-Bird.radius
        Bird.vy=-Bird.vy*0.9
    Bird.x+=Bird.vx*dt
    if Bird.x > WIDTH-Bird.radius or Bird.x < Bird.radius:
        Bird.vx=-Bird.vx
def on_key_down(key):
    if key==keys.SPACE:
        Bird.vy=-500
pgzrun.go()