import pygame,math
from Drawable import Drawable
from math import cos,sin,asin,radians
from Lines import Lines

class LineRect(Drawable):
    def __init__(self, surface: pygame, pos : tuple , lineslast : list,linesfirst : list ) -> None:
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
        self.laserangle=0

        self.linesf=linesfirst
        self.linesl=lineslast

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
        self.laserpoints(self.linesf,self.linesl)   

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


#Lasers

    # def barr(self,liner):
    #     ml=[]
    #     for i in range(len(self.liner.linesf)):
    #         m=(liner.linesl[i][1]-liner.linesf[i][1])/(liner.linesl[0]-liner.linesf[0])
    #         ml.append(m)
    #     return ml
    # def barrDetector(self,fp):
    #     # if one laser crops an line 
    #     mlist=self.barr(self.liner)
    #     for i in self.lasersLastPoints:
    #         for j in range(len(self.liner.linesf)):
    #             # first condition is if laser's first point's x is lower then barrier's first point's x and laser's last point's x is higher then barrier's last point's x ....  
    #             if ((fp[0]<self.liner.linesf[j][0] and i[0]>self.liner.linesl[j][0]) or (fp[1]<self.liner.linesf[j][1] and i[1]>self.liner.linesl[1]) ) or ( (fp[0]>self.liner.linesf[j][0] and i[0]<self.liner.linesl[j][0]) or (fp[1]>self.liner.linesf[j][1] and i[1]<self.liner.linesl[1])):
    #                 self.lasersLastPoints[i]=50
    
    @staticmethod
    def barrfunc(linesf:list,linesl:list):
        ml=[]
        for i in range(len(linesf)):
            m=(linesf[i][1]-linesl[i][1])/(linesf[i][0]-linesl[i][0])
            b=linesf[i][1]-m*linesf[i][0]
            ml.append((m,b))
        return ml
    def laserfunc(self,fp:tuple,las:tuple):
        #las is one lasers last point
        m=(fp[1]-las[1])/(fp[0]-las[0])
        b=fp[1]-m*fp[0]
        return (m,b)

    
    def closestbar(self,fp:tuple,laslast:tuple,linesf:list,linesl:list):
        clist=[]
        cbool=False
        laser=self.laserfunc(fp,laslast)
        for i in range(len(linesf)):
            # if x of laser' first point lower then x of line's first point and x of last point of laser higher then x of line's last point  
            #((linesf[i][0]<fp[0] and linesl[i][0]>laslast[0] and (fp[0]<linesl[i][0] or laslast[0]>linesf[i][0]) ) or (linesf[i][0]>fp[0] and linesl[i][0]<laslast[0] and (fp[0]<linesl[i][0] or laslast[0]>linesf[i][0])) ) or (linesl[i][1]<laslast[1] and fp[1]<linesf[i][1] and (fp[1]<linesl[i][1] or laslast[1]>linesf[i][1])) or (linesl[i][1]>laslast[1] and fp[1]>linesf[i][1] and (fp[1]<linesl[i][1] or laslast[1]>linesf[i][1]))
            if (laser[0]*linesf[i][0]+laser[1] < linesf[i][1] and laser[0]*linesl[i][0]+laser[1] > linesl[i][1]) or (laser[0]*linesf[i][0]+laser[1] > linesf[i][1] and laser[0]*linesl[i][0]+laser[1] < linesl[i][1]) :
                barr=self.barrfunc(linesf,linesl)[i]
                las=self.laserfunc(fp,laslast)
                x=(barr[1]-las[1])/(las[0]-barr[0])
                y=las[0]*x+las[1]
                if self.pointdist(laslast,fp)>self.pointdist(laslast,(x,y)):
                    clist.append(i)
                    cbool=True

        return (cbool,clist)


    def lasercut(self,fp:tuple,las:tuple,linesf:list,linesl:list,closest:int):
        laser=self.laserfunc(fp,las)
        # Barrier's m and b
        barrsList=self.barrfunc(linesf,linesl)
        # if the closestpoint is our laser's max distance
        # if closest is tuple:
        #     return closest
       
        # x= d-b / a-c  |  y=ax+b(lasers func)=cx+d (barr func)
        x=(barrsList[closest][1]-laser[1])/(laser[0]-barrsList[closest][0])
        y=laser[0]*x + laser[1]
        #these are ours new x and y values. we will assign these values at laser's new last point
        return (x,y)
    
    
    @staticmethod
    def pointdist(p1:tuple,p2:tuple):
        return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2


    def laserpoints(self,linesf,linesl):
        #lasers 1. poin is middle point. 
        fp=((self.p1[0]+self.p3[0])/2,(self.p1[1]+self.p3[1])/2)
        dist=200   
        self.laserangle+=radians(0.2)
        rotatedist=(dist*cos(self.laserangle),dist*sin(self.laserangle))
        # laser points by rotate factor
        #  0-----0-----0
        #
        self.lasersLastPoints= [(fp[0]+rotatedist[0],fp[1]+rotatedist[1]),(fp[0]+dist*cos(self.laserangle+radians(90)),fp[1]+dist*sin(self.laserangle+radians(90))),(fp[0]+dist*cos(self.laserangle+radians(180)),fp[1]+dist*sin(self.laserangle+radians(180))),(fp[0]+dist*cos(self.laserangle+radians(-90)),fp[1]+dist*sin(self.laserangle+radians(-90)))]
        # laserpoint 4 için deneme Bunu tüm laserler için dönecez
        for j in range(len(self.lasersLastPoints)):
            barfinder=self.closestbar(fp,self.lasersLastPoints[j],linesf,linesl)
            # barfinder[1].append(self.lasersLastPoints[3])
            # last item of barfinder means self.laserLastPoints[3]
            closestBarr=len(barfinder[1])-1
            if barfinder[0]:
                for i in barfinder[1]:
                    if self.pointdist(fp,self.lasercut(fp,self.lasersLastPoints[j],linesl,linesf,closestBarr))> self.pointdist(fp,self.lasercut(fp,self.lasersLastPoints[j],linesl,linesf,i)):#barfinder[1][i]
                        closestBarr=i
                if self.pointdist(fp,self.lasercut(fp,self.lasersLastPoints[j],linesl,linesf,closestBarr)) < 200**2:
                    self.lasersLastPoints[j]=self.lasercut(fp,self.lasersLastPoints[j],linesl,linesf,closestBarr)
            # self.barrDetector(fp)
        for i in self.lasersLastPoints:
            pygame.draw.line(self.surface,self.color,fp,i,2)
    
    # pressing gas
    def move(self,forw=False,back=False):
        rad=self.angle
        y=math.sin(rad)*self.speed[1]
        x=math.cos(rad)*self.speed[0]
    
        self.p1=(self.p1[0]+x,self.p1[1]+y)
        self.p2=(self.p2[0]+x,self.p2[1]+y)
        self.p3=(self.p3[0]+x,self.p3[1]+y)
        self.p4=(self.p4[0]+x,self.p4[1]+y)
        self.drawrect()
