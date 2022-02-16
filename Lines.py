import pygame
from Drawable import Drawable


class Lines(Drawable):

    def __init__(self, surface : pygame.Surface,linesf,linesl) -> None:
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

        