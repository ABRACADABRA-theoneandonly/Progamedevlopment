import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
class Shapes():
    def __init__(self,color,pos,width,height):
        self.s = screen
        self.c = color
        self.p = pos
        self.x=pos[0]
        self.y=pos[1]
        self.h = height
        self.w = width
    def draw(self):
        pygame.draw.rect(self.s,self.c,(self.x,self.y,self.w,self.h))
    def grow(self,size):
        self.h += size
        self.w += size
        pygame.draw.rect(self.s,self.c,(self.x,self.y,self.w,self.h))
A = Shapes("blue",(50,100),60,200)
B = Shapes("red",(100,100),70,180)
C = Shapes("purple",(150,100),80,100)
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            A.draw()
            B.draw()
            C.draw()
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            A.grow(10)
            B.grow(10)
            C.grow(10)
            pygame.display.update()
        elif i.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            X = Shapes("orange", pos, 20, 30)
            X.draw()
            pygame.display.update()