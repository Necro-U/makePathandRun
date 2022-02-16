import pygame
from Rectangle import Rectangle


class UiElements(Rectangle):
    def __init__(self, surface : pygame, pos : tuple,weight : int ,length : int) -> None:
        super().__init__(surface,pos,weight,length)

    


    def drawUi(self):
        self.drawRect()
