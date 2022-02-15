import carclasses as cr
import sys, pygame
pygame.init()

size = width, height = 1200,1000
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
screen.set_colorkey((255,255,0))



#line arrays
linearrF=[]
linearrL=[]
notshow=[]

# mod booleans
editbool=True
drivebool=False
runModeBool=False

careditbool=True
lineeditbool=False
lineshowerbool=False
lineshowerbool2=False


drawLines=False
drawLine=False
finishreload=True
#car bools
carcreated=False
forwardbool=False
moved=False
# creating objects
carrect=cr.Rectangle(screen,(1000,0),150,0)
moder=cr.Appmode(screen)
liner=cr.Lines(screen,linearrF,linearrL)

while 1:
    screen.fill((0,120,120))
    #Creating continious objects 
    mouspos=pygame.mouse.get_pos()
    mousx=mouspos[0]
    mousy=mouspos[1]
    #Events 
    keys=pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        

        if editbool:
            # line editting and creating line object(s)
            if lineeditbool:
                # downpos=pygame.mouse.get_pos()
                careditbool=False
                if not (mousx>900 and mousy<150):
                    
                    if event.type==pygame.MOUSEBUTTONUP :
                        linearrF.append(downpos)
                        linearrL.append(uppos)
                        finishreload=True
                        drawLines=True

                    if pygame.mouse.get_pressed()[0]:
                        if event.type==pygame.MOUSEBUTTONDOWN :
                            downpos=pygame.mouse.get_pos()
                            finishreload=False
                            drawLine=True
                            lineshowerbool=True
                    if pygame.mouse.get_pressed()[2]:
                        
                        posit=pygame.mouse.get_pos()
                        # print(linearrF[0][0],posit[0])
                        
                        for i in range(len(linearrF)):
                            if ((posit[0]-linearrF[i][0])**2+(posit[1]-linearrF[i][1])**2)<=9:
                                notshow.append(linearrF[i])
                            
       
                                
                            
                            
                      

            # Car editting and creating car object
            if careditbool:
                lineeditbool=False
                if event.type==pygame.MOUSEBUTTONDOWN and not (mousx>900 and mousy<150): 
                    
                    carcreated=True
                    mycar=cr.LineRect(screen,mouspos)

        # clicking rectangles
        if event.type==pygame.MOUSEBUTTONDOWN:
            if mousx>1050 and mousy<150: 
                careditbool=True
                lineeditbool=False
            elif 900<mousx<1050 and mousy<150: 
                lineeditbool=True 
                careditbool=False


    # Events - setting mod booleans
    if keys[pygame.K_e] :
        editbool=True
        drivebool=False
        runModeBool=False    

    if keys[pygame.K_r]:
        drivebool=True
        editbool=False  
        runModeBool=True    
    
    #editting
    if editbool:
        if careditbool:
            moder.editting(cardaw=True)
        elif lineeditbool:
            moder.editting(linedraw=True)
            # liner.creatingline(mousx,mousy)
    if runModeBool:
        moder.driving()


            
    if lineshowerbool:
        if not finishreload:
            uppos=pygame.mouse.get_pos()

        if drawLine:
            # pygame.draw.line(screen,(150,150,150),downpos,uppos,3)
            liner.drawSingleLine(downpos,uppos,notshow)


        if drawLines:
            for i in range(len(linearrF)):
                # pygame.draw.line(screen,(150,150,150),linearrF[i],linearrL[i],3)
                liner.drawSingleLine(linearrF[i],linearrL[i],notshow)
                



    #driving
    if carcreated:    
        if editbool:
            mycar.drawrect()


        if drivebool:
            
            if keys[pygame.K_a]:
        # linerect.rotaterect(left=True)
                mycar.angle-=mycar.rotvel
                mycar.rotateByMiddot()
            elif keys[pygame.K_d]:
                # linerect.rotaterect(right=True)
                mycar.angle+=mycar.rotvel
                mycar.rotateByMiddot()


            if keys[pygame.K_w]:
                mycar.move_forward()
                moved=True
            if keys[pygame.K_s]:
                mycar.move_backward()
                moved=True

            moved=False            

            if not moved:
                mycar.reduce_speed()
            
    # pygame.draw.lines(screen,(0,255,0),True,[(300,300),(300,340),(340,340),(340,300)])
    # myrect.drawRect()
    
    # myrect.carblit()

    pygame.display.flip()
