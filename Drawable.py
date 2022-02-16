import pygame

class Drawable():

    def __init__(self,surface : pygame.Surface,pos:tuple) -> None:
        self.surface=surface
        self.pos=pos