from math import cos, radians, sin ,asin
import pygame,math

class Drawable():

    def __init__(self,surface : pygame,pos) -> None:
        self.surface=surface
        self.pos=pos

class TextRenderer(Drawable):
    def __init__(self,surface : pygame,text, pos) -> None:
        super().__init__(surface, pos)
        self.textfont='freesansbold.ttf'
        self.textsize=20
        self.color=(155,155,155)
        self.text=text

    def typer(self):
        yazi=pygame.font.Font(self.textfont,self.textsize).render(self.text,True,self.color)
        self.surface.blit(yazi,self.pos)






class Lines(Drawable):

    def __init__(self, surface : pygame,linesf,linesl) -> None:
        self.surface=surface
        self.lastpos=(0,0)
        self.pos=(0,0)
        #lines positions arrays first-last
        self.linesf=linesf
        self.linesl=linesl
        self.width=2

        self.deleterR=5
        
        self.leftclick=False
        self.linefinish=False
        self.lineBool=False
      
    def drawSingleLine(self,firstpos,lastpos,notshower):
        if firstpos not in notshower:
            fx=firstpos[0]
            fy=firstpos[1]
            lx=lastpos[0]
            ly=lastpos[1]
            pygame.draw.line(self.surface,(200,200,200),firstpos,lastpos,self.width)
            pygame.draw.circle(self.surface,(255,0,0),firstpos,8)
            pygame.draw.circle(self.surface,(255,0,0),((fx+lx)/2,(fy+ly)/2),8)
            pygame.draw.circle(self.surface,(255,0,0),lastpos,8)

        
    def deletingline(self):
        self.pos=pygame.mouse.get_pos()
        for i in range(len(self.linesf)):
            if (self.pos[0]-self.linesf[i][0])**2+(self.pos[1]-self.linesf[i][1])**2<=self.deleterR**2:
                self.linesf.pop(i)
                self.linesl.pop(i)

        

    def drawLines(self,notshow):
        if self.lineBool :
            if len(self.linesf)>1:
                for i in range(len(self.linesf)):
                    if i in notshow:
                        pass
                    else:
                        pygame.draw.line(self.surface,(200,200,200),self.linesf[i],self.linesl[i],self.width)
            pygame.draw.line(self.surface,(200,200,200),self.pos,self.lastpos,self.width)

    def creatingline(self,evtype,mousex,mousey):
        
        # event.type==pygame.MOUSEBUTTONDOWN and 
        
        if not(mousex>900 and mousey<150): 
            if evtype== pygame.MOUSEBUTTONDOWN:

                    if pygame.mouse.get_pressed()[0]:
                    # getting first pos of line
                        self.pos=pygame.mouse.get_pos()
                    # we created a line!
                        self.lineBool=True
                    # Line not finished yet
                        self.linefinish=True
                    # left clicled
                        self.leftclick=True
                    
                    if pygame.mouse.get_pressed()[2]:
                        self.pos=pygame.mouse.get_pos()
                        for i in range(len(self.linesf)):
                            if (self.pos[0]-self.linesf[i][0])**2+(self.pos[1]-self.linesf[i][1])**2<=9:
                                self.linesf.pop(i)
                                


            if evtype==pygame.MOUSEBUTTONUP:
                if self.leftclick:
                    # finish pos of line
                    self.linefinish=False
                    # add them to lines list
                    self.linesf.append(self.pos)
                    self.linesl.append(self.lastpos)

        if self.linefinish:
            self.lastpos=pygame.mouse.get_pos()

        


        # if self.lineBool and len(self.linesf)>1:
        #     for i in range(len(self.linesf)):
        #         pygame.draw.line(self.surface,(200,200,200),self.linesf[i],self.linesl[i],self.width)
        # elif self.lineBool :
        #     pygame.draw.line(self.surface,(200,200,200),self.pos,self.lastpos,self.width)
    

class LineRect(Drawable):
    def __init__(self, surface: pygame, pos) -> None:
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
        # 1. line self.p1, self.p2 r=w/2   rotasyon yaparken buralarda bir sorun var!!!!!
        # self.rotarr=[(self.p1[0],self.p1[1]+self.height/2),(self.p1[0]+self.weight,self.p1[1]+self.height)] 
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
        # elif back:
        #     self.p1=(self.p1[0]x,self.p1[1]-y)
        #     self.p2=(self.p2[0]-x,self.p2[1]-y)
        #     self.p3=(self.p3[0]-x,self.p3[1]-y)
        #     self.p4=(self.p4[0]-x,self.p4[1]-y)
        self.drawrect()

        
# rectangle
class Rectangle(Drawable):
    
    def __init__(self, surface : pygame,pos,weight,length) -> None:
        super().__init__(surface,pos)
        self.weight=weight
        self.length=length
        self.x=self.pos[0]
        self.y=self.pos[1]
        # self.weight=40
        # self.length=60
        self.drawed=False
        # self.rect=pygame.draw.lines(self.surface,(0,255,0),True,[self.pos,(self.x,self.y+self.length),(self.x+self.weight,self.y+self.length),(self.x+self.weight,self.y)])
        self.mysurf=pygame.Surface((self.length,self.weight))
        self.myrect=self.mysurf.get_rect(topleft=pos)
    def drawRect(self):
    #     pygame.draw.lines(self.surface,(0,255,0),True,[self.pos,(self.x,self.y+self.length),(self.x+self.weight,self.y+self.length),(self.x+self.weight,self.y)])
        
        # pygame.draw.rect(self.surface,(150,150,150),self.myrect,1)
        self.surface.blit(self.mysurf,self.myrect.topleft)
    

    # def delRect(self):
    #     x,y= pygame.mouse.get_pos()
    #     if (self.pos[0]-x)**2+(self.pos[1]-y)**2<=3:
    #         self.drawed=False



class UiElements(Rectangle):
    def __init__(self, surface : pygame, pos,weight,length) -> None:
        super().__init__(surface,pos,weight,length)

    


    def drawUi(self):
        self.drawRect()



def blit_rotate_center(screen,surface,top_left,angle):
        newsurf=pygame.transform.rotate(surface,angle)
        new_rect=newsurf.get_rect(center=surface.get_rect(topleft=top_left).center)
        # self.myrect=new_rect
        # self.mysurf=newsurf
        screen.blit(newsurf,new_rect.topleft)


# You can create a car and drive it but its a image. Rejected go check linerect
class Car(UiElements):
    IMG=pygame.image.load('purple-car.png')
    def __init__(self,surface : pygame.Surface,pos) -> None:
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
        # pygame.Surface((self.length, self.weight))



class Appmode():

    def __init__(self,screen) -> None:
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