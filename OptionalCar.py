from UiElements import UiElements
import pygame
import math


def blit_rotate_center(screen,surface,top_left,angle):
        newsurf=pygame.transform.rotate(surface,angle)
        new_rect=newsurf.get_rect(center=surface.get_rect(topleft=top_left).center)
        screen.blit(newsurf,new_rect.topleft)


# You can create a car and drive it but its a image. Rejected go check linerect
class Car(UiElements):
    IMG=pygame.image.load('purple-car.png')
    def __init__(self,surface : pygame.Surface.subsurface,pos : tuple) -> None:
        super().__init__(surface,pos,40,60)
        self.speed=0
        self.rot_speed=0.2
        self.angle=0
        self.img=self.IMG
        self.maxsp=0.8
        self.acc=0.05
        self.forwbool=False
        self.backbool=False

    def showcar(self):
        self.surface.blit(self.img,(self.x,self.y))

    def move_forward(self):
        self.forwbool=True
        self.backbool=False

        self.speed=min(self.speed+self.acc,self.maxsp)
        self.move()
    
    def move_backward(self):
        # set forward backward  boolleans
        self.backbool=True
        self.forwbool=False

        self.speed=max(self.speed-self.acc,-self.maxsp)
        self.move()

    def move(self):
        rad=math.radians(self.angle)
        y=math.cos(rad)*self.speed
        x=math.sin(rad)*self.speed
        self.x-=x
        self.y-=y
    

    def reduce_speed(self):
        if self.forwbool:
            self.speed=max(self.speed-0.002,0)
        elif self.backbool:
            self.speed=min(self.speed+0.002,0)
        self.move()

    def setbool0(self):
        if self.speed==0:
            self.forwbool=False
            self.backbool=False

    def updateangle(self,right=False,left=False):
        if left:
            self.angle+=self.rot_speed
        if right:
            self.angle-=self.rot_speed
            


    def drive(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.updateangle(left=True)           
        elif key[pygame.K_d]:
            self.updateangle(right=True)  
        self.rotate()
        if key[pygame.K_w]:
            self.move_forward()

        elif key[pygame.K_s]:
            self.move_backward()
        self.setbool0()

        
        
    
    
    def rotate(self):
        blit_rotate_center(self.surface,self.img,(self.x,self.y),self.angle)