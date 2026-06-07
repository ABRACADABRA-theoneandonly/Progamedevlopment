import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
class Shapes():
    def __init__(self,color,pos,radius,width):
        self.s=screen
        self.c=color
        self.p=pos
        self.r=radius
        self.w=width
    def draw(self):
        pygame.draw.circle(self.s,self.c,self.p,self.r,self.w)
    def grow(self,size):
        self.r+=size
        pygame.draw.circle(self.s,self.c,self.p,self.r,self.w)
A=Shapes("blue",(300,300),60,200)
B=Shapes("red",(300,300),70,180)
C=Shapes("Purple",(300,300),80,100)
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.MOUSEBUTTONDOWN:
            A.draw()
            B.draw()
            C.draw()
            pygame.display.update()
        elif i.type==pygame.MOUSEBUTTONUP:
            A.grow(10)
            B.grow(10)
            C.grow(10)
            pygame.display.update()
        elif i.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            X=Shapes("orange",pos,20,30)
            X.draw()
            pygame.display.update()