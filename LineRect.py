import pygame,math
from Drawable import Drawable
from math import cos,sin,asin,radians


class LineRect(Drawable):
    def __init__(self, surface: pygame, pos : tuple) -> None:
        super().__init__(surface, pos)
        self.weight=80
        self.height=40
        self.color=(0,255,0)
        self.x=self.pos[0]
        self.y=self.pos[1]
        self.angle=radians(0)
        self.p1,self.p2,self.p3,self.p4=(self.x,self.y),(self.x+self.weight,self.y),(self.x+self.weight,self.y+self.height),(self.x,self.y+self.height)
        self.speed=[0.1,0.1]
        self.maxvel=0.8
        self.rotvel=radians(0.4)
        self.acc=0.02

        self.backbool=False
        self.forwbool=False

        
        # sometihng about rotating by midline
        self.rotarr=[(self.p1[0]+(self.height/2)*sin(self.angle),self.p1[1]+(self.height/2)*cos(self.angle)),(self.p2[0]+(self.height/2)*sin(self.angle),self.p2[1]+(self.height/2)*cos(self.angle))]
        
        
        # about rotating by middledot
        self.r=pow((self.weight/2)**2+(self.height/2)**2,1/2)
        self.middot=((self.p1[0]+self.p3[0])/2,(self.p1[1]+self.p3[1])/2)
        # arccos of L/2r for each dots a1=p1 ...
        self.a1=[radians(180)-asin(self.height/(2*self.r)),radians(180)-asin(self.height/(2*self.r))]
        self.a2=[asin(self.height/(2*self.r)),asin(self.height/(2*self.r))]
        self.a3=[-asin(self.height/(2*self.r)),-asin(self.height/(2*self.r))]
        self.a4=[radians(180)+asin(self.height/(2*self.r)),radians(180)+asin(self.height/(2*self.r))]

    def rotateByMiddot(self):
        self.middot=((self.p1[0]+self.p3[0])/2,(self.p1[1]+self.p3[1])/2)
        self.p1=(self.middot[0]+cos(self.a1[0]+self.angle)*self.r,self.middot[1]+sin(self.a1[1]+self.angle)*self.r)
        self.p2=(self.middot[0]+cos(self.a2[0]+self.angle)*self.r,self.middot[1]+sin(self.a2[1]+self.angle)*self.r)
        self.p3=(self.middot[0]+cos(self.a3[0]+self.angle)*self.r,self.middot[1]+sin(self.a3[1]+self.angle)*self.r)
        self.p4=(self.middot[0]+cos(self.a4[0]+self.angle)*self.r,self.middot[1]+sin(self.a4[1]+self.angle)*self.r)



    def drawrect(self):
        pygame.draw.lines(self.surface,self.color,True,[self.p1,self.p2,self.p3,self.p4],3)    

    # trying rotate by middle line but something gone wrong
    def rotateMiddleLine(self):
        radious=self.weight/2
        midleline=self.rotarr
        newmidleiLine=[(midleline[0][0]+radious*(1-cos(self.angle)),midleline[0][1]+radious*sin(self.angle)),(midleline[1][0]-radious*(1-cos(self.angle)),midleline[0][1]-radious*sin(self.angle))]
        return newmidleiLine
    
    # again rotating by midleline not used
    def rotaterect(self,right=False,left=False):
        mid=self.rotateMiddleLine()
        
        
        self.p1=(mid[0][0]-sin(self.angle)*(self.height/2),mid[0][1]-cos(self.angle)*(self.height/2))
        self.p4=(mid[1][0]-sin(self.angle)*(self.height/2),mid[1][1]-cos(self.angle)*(self.height/2))

        self.p2=(mid[0][0]+sin(self.angle)*(self.height/2),mid[0][1]+cos(self.angle)*(self.height/2))
        self.p3=(mid[1][0]+sin(self.angle)*(self.height/2),mid[1][1]+cos(self.angle)*(self.height/2))
        if right:
            self.angle-=self.rotvel
        if left:
            self.angle+=self.rotvel

        # self.refreshpoints()
        self.drawrect()


    def move_forward(self):
        self.forwbool=True
        self.backbool=False

        self.speed=[min(self.speed[0]+self.acc,self.maxvel),min(self.speed[1]+self.acc,self.maxvel)]
        self.move(forw=True,back=False)
    
    def move_backward(self):
        # set forward backward  boolleans
        self.backbool=True
        self.forwbool=False

        self.speed=[max(self.speed[0]-self.acc,-self.maxvel),max(self.speed[1]-self.acc,-self.maxvel)]
        self.move(back=True,forw=False)


    def reduce_speed(self):
        if self.forwbool:
            self.speed=[max(self.speed[0]-0.005,0),max(self.speed[1]-0.005,0)]
            self.move(forw=True,back=False)
        elif self.backbool:
            self.speed=[min(self.speed[0]+0.005,0),min(self.speed[1]+0.005,0)]
            self.move(back=True,forw=False)
        else:
            self.drawrect()


    # pressing gas
    def move(self,forw=False,back=False):
        rad=self.angle
        y=math.sin(rad)*self.speed[1]
        x=math.cos(rad)*self.speed[0]
        # if forw:
        self.p1=(self.p1[0]+x,self.p1[1]+y)
        self.p2=(self.p2[0]+x,self.p2[1]+y)
        self.p3=(self.p3[0]+x,self.p3[1]+y)
        self.p4=(self.p4[0]+x,self.p4[1]+y)
        self.drawrect()
