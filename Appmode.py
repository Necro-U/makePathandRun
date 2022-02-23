import pygame
from Rectangle import Rectangle
from TextRenderer import TextRenderer


class Appmode():

    def __init__(self,screen : pygame.Surface.subsurface) -> None:
        self.screen=screen
        self.linedit=False
        self.caredit=False
        #rect of car
        self.carrect=Rectangle(self.screen,(1050,0),150,150)
        # text of car in the rect
        self.carrecttext=TextRenderer(self.screen,'Car',(1120,80))
        # text of car at bottom
        self.carrecttextBot=TextRenderer(self.screen,'Car Editing',(590,940))
        #rect of Line
        self.linerect=Rectangle(self.screen,(900,0),150,150)
        # text of line in the rect
        self.linerecttext=TextRenderer(self.screen,'Line',(965,80))
        # text of line at bottom
        self.linerecttextBot=TextRenderer(self.screen,'Line Editing',(590,940))
        # text of diriving bottom
        self.driverTextBot=TextRenderer(self.screen,'Run!',(590,940))


    
    def editting(self,cardaw=False,linedraw=False): 
        #typing car's texts     
        self.carrect.drawRect()
        self.carrecttext.typer()
        self.linerect.drawRect()
        self.linerecttext.typer()
        if cardaw:
            self.carrecttextBot.typer()
        # typing line's texts
        
        elif linedraw :
            self.linerecttextBot.typer()
    
    def driving(self):
        self.driverTextBot.typer()