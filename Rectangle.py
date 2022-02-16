from Drawable import Drawable
import pygame

class Rectangle(Drawable):
    
    def __init__(self, surface : pygame,pos : tuple,weight : int ,length : int) -> None:
        super().__init__(surface,pos)
        self.weight=weight
        self.length=length
        self.x=self.pos[0]
        self.y=self.pos[1]
        self.drawed=False
        self.mysurf=pygame.Surface((self.length,self.weight))
        self.myrect=self.mysurf.get_rect(topleft=pos)
    def drawRect(self):
        self.surface.blit(self.mysurf,self.myrect.topleft)
    