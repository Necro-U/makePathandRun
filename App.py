from Appmode import Appmode
import sys, pygame
from Appmode import Appmode
from TextRenderer import TextRenderer 
from Rectangle import Rectangle 
from OptionalCar import Car 
from Lines import Lines 
from LineRect import LineRect 
from Drawable import Drawable 
from UiElements import UiElements 





class App():

    def __init__(self) -> None:
        self.size = self.width, self.height = 1200,1000
        self.speed = [2, 2]
        self.black = 0, 0, 0

        self.screen = pygame.display.set_mode(self.size)
        self.screen.set_colorkey((255,255,0))
        #line arrays
        self.linearrF=[]
        self.linearrL=[]
        self.notshow=[]

        # mod booleans
        self.editbool=True
        self.drivebool=False
        self.runModeBool=False

        self.careditbool=True
        self.lineeditbool=False
        self.lineshowerbool=False
        self.lineshowerbool2=False


        self.drawLines=False
        self.drawLine=False
        self.finishreload=True
        #car bools
        self.carcreated=False
        self.forwardbool=False
        self.moved=False
        # creating objects
        self.carrect=Rectangle(self.screen,(1000,0),150,0)
        self.moder=Appmode(self.screen)
        self.liner=Lines(self.screen,self.linearrF,self.linearrL)


    def eventprogressor(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]  :
                    sys.exit() 
                

                if self.editbool:
                    # line editting and creating line object(s)
                    if self.lineeditbool:
                        # downpos=pygame.mouse.get_pos()
                        careditbool=False
                        if not (self.mousx>900 and self.mousy<150):
                            
                            if event.type==pygame.MOUSEBUTTONUP :
                                self.linearrF.append(self.downpos)
                                self.linearrL.append(self.uppos)
                                self.finishreload=True
                                self.drawLines=True

                            if pygame.mouse.get_pressed()[0]:
                                if event.type==pygame.MOUSEBUTTONDOWN :
                                    self.downpos=pygame.mouse.get_pos()
                                    self.finishreload=False
                                    self.drawLine=True
                                    self.lineshowerbool=True
                            if pygame.mouse.get_pressed()[2]:
                                
                                posit=pygame.mouse.get_pos()
                                # print(linearrF[0][0],posit[0])
                                
                                for i in range(len(self.linearrF)):
                                    if ((posit[0]-self.linearrF[i][0])**2+(posit[1]-self.linearrF[i][1])**2)<=9:
                                        self.notshow.append(self.linearrF[i])
                                    
            
                                        
                                    
                                    
                            

                    # Car editting and creating car object
                    if self.careditbool:
                        self.lineeditbool=False
                        if event.type==pygame.MOUSEBUTTONDOWN and not (self.mousx>900 and self.mousy<150): 
                            
                            self.carcreated=True
                            self.mycar=LineRect(self.screen,self.mouspos)

                # clicking rectangles
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.mousx>1050 and self.mousy<150: 
                        self.careditbool=True
                        self.lineeditbool=False
                    elif 900<self.mousx<1050 and self.mousy<150: 
                        self.lineeditbool=True 
                        self.careditbool=False


    def modchanger(self):
        # Events - setting mod booleans
            if self.keys[pygame.K_e] :
                self.editbool=True
                self.drivebool=False
                self.runModeBool=False    

            if self.keys[pygame.K_r]:
                self.drivebool=True
                self.editbool=False  
                self.runModeBool=True    
            
    def editer(self):
        if self.editbool:
                if self.careditbool:
                    self.moder.editting(cardaw=True)
                elif self.lineeditbool:
                    self.moder.editting(linedraw=True)
                    # liner.creatingline(mousx,mousy)
        if self.runModeBool:
            self.moder.driving()


                
        if self.lineshowerbool:
            if not self.finishreload:
                self.uppos=pygame.mouse.get_pos()

            if self.drawLine:
                # pygame.draw.line(screen,(150,150,150),downpos,uppos,3)
                self.liner.drawSingleLine(self.downpos,self.uppos,self.notshow)


            if self.drawLines:
                for i in range(len(self.linearrF)):
                    # pygame.draw.line(screen,(150,150,150),linearrF[i],linearrL[i],3)
                    self.liner.drawSingleLine(self.linearrF[i],self.linearrL[i],self.notshow)
                    

    def driver(self):
        #driving
        if self.carcreated:    
            if self.editbool:
                self.mycar.drawrect()


            if self.drivebool:
                
                if self.keys[pygame.K_a]:
            # linerect.rotaterect(left=True)
                    self.mycar.angle-=self.mycar.rotvel
                    self.mycar.rotateByMiddot()
                elif self.keys[pygame.K_d]:
                    # linerect.rotaterect(right=True)
                    self.mycar.angle+=self.mycar.rotvel
                    self.mycar.rotateByMiddot()


                if self.keys[pygame.K_w]:
                    self.mycar.move_forward()
                    moved=True
                if self.keys[pygame.K_s]:
                    self.mycar.move_backward()
                    moved=True

                moved=False            

                if not moved:
                    self.mycar.reduce_speed()
                


    def Runner(self):

        pygame.init()

        




        while 1:
            self.screen.fill((0,120,120))
            #Creating continious objects 
            self.mouspos=pygame.mouse.get_pos()
            self.mousx=self.mouspos[0]
            self.mousy=self.mouspos[1]
            #Events 
            self.keys=pygame.key.get_pressed()

            self.eventprogressor()

            self.modchanger()

            
            self.editer()

            self.driver()

            
            pygame.display.flip()
