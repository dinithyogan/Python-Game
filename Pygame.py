import pygame, sys
from pygame.locals import *
import random
ret1=Rect(0,400,100,100)
ret2=Rect(400,400,100,100)
RectangleObjects=[ret1,ret2]
l=11
r=0
list1=[0,1,2,3,4,5,6,7,8,9,10,11]
def options():
    pygame.draw.rect(Window,(255,0,0),Rect(0,400,100,100),5)
    pygame.draw.rect(Window,(255,0,0),Rect(400,400,100,100),5)
def word():
    slide1l = myfont.render('Previous', False, (0, 0, 0))
    Window.blit(slide1l,(15,440))
    slide1r = myfont.render('Next', False, (0, 0, 0))
    Window.blit(slide1r,(425,440))
def recNumber(mouse_position):
    for i in range(2):
        global l
        global r
        if(l==11 and r==0 and RectangleObjects[0].collidepoint(mouse_position)):
            r+=1
            l-=1
            return r,l
            
        if RectangleObjects[i].collidepoint(mouse_position):
            if(i+1==1):
                l+=1
                r-=1
                if((r not in list1) or (l not in list1)):
                    l-=1
                    r+=1
                    return -1,-1
                return r,l
            elif(i+1==2):
                r+=1
                l-=1
                if((r not in list1) or (l not in list1)):
                    l+=1
                    r-=1
                    return -1,-1
                return r,l
    return -1,-1
def main():
    pygame.init()
    global Window
    global r1
    global l1
    global myfont
    r1=0
    l1=11
    Window = pygame.display.set_mode((500,500))
    Window.fill((255,255,255))
    pygame.display.update()
    pygame.display.set_caption('First Game')
    myfont = pygame.font.SysFont('Comic Sans MS',16,True)
    myfont1 = pygame.font.SysFont('Comic Sans MS',36,True)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif ( event.type == pygame.MOUSEBUTTONUP ):
                mouse_position = pygame.mouse.get_pos()
                r1,l1=recNumber(mouse_position)
                if(r1==1 and l1==10):
                    Window.fill((255,255,255))
                    options()
                    word()
                    slide12 = myfont1.render('Think a number', False, (0, 0, 0))
                    Window.blit(slide12,(120,200))
                    pygame.display.update()
                if(r1==2 and l1==9):
                    Window.fill((255,255,255))
                    options()
                    word()
                    ab1="Multiply by "+str(z)
                    slide12 = myfont1.render(ab1, False, (0, 0, 0))
                    Window.blit(slide12,(130,200))
                    pygame.display.update()
                if(r1==3 and l1==8):
                    Window.fill((255,255,255))
                    options()
                    word()
                    ab2="Add by "+str(m)
                    slide12 = myfont1.render(ab2, False, (0, 0, 0))
                    Window.blit(slide12,(160,200))
                    pygame.display.update()
                if(r1==4 and l1==7):
                    Window.fill((255,255,255))
                    options()
                    word()
                    ab3="Divide by "+str(z)
                    slide12 = myfont1.render(ab3, False, (0, 0, 0))
                    Window.blit(slide12,(145,200))
                    pygame.display.update()
                if(r1==5 and l1==6):
                    Window.fill((255,255,255))
                    options()
                    word()
                    slide12 = myfont1.render('Current no - Thinked no', False, (0, 0, 0))
                    Window.blit(slide12,(45,200))
                    pygame.display.update()
                if(r1==6 and l1==5):
                    Window.fill((255,255,255))
                    options()
                    word()
                    ab4='Multiply by '+str(n)
                    slide12 = myfont1.render(ab4, False, (0, 0, 0))
                    Window.blit(slide12,(125,200))
                    pygame.display.update()
                if(r1==7 and l1==4):
                    Window.fill((255,255,255))
                    options()
                    word()
                    ab5='Add by '+str(o)
                    slide12 = myfont1.render(ab5, False, (0, 0, 0))
                    Window.blit(slide12,(160,200))
                    pygame.display.update()
                if(r1==8 and l1==3):
                    Window.fill((255,255,255))
                    options()
                    word()
                    ab6='Subtract by '+str(p)
                    slide12 = myfont1.render(ab6, False, (0, 0, 0))
                    Window.blit(slide12,(125,200))
                    pygame.display.update()
                if(r1==9 and l1==2):
                    Window.fill((255,255,255))
                    options()
                    word()
                    ab7='Multiply by '+str(q)
                    slide12 = myfont1.render(ab7, False, (0, 0, 0))
                    Window.blit(slide12,(125,200))
                    pygame.display.update()
                if(r1==10 and l1==1):
                    Window.fill((255,255,255))
                    options()
                    word()
                    myfont6 = pygame.font.SysFont('Comic Sans MS',60,True)
                    textsurface = myfont6.render('You did it!', False, (0, 0, 0))
                    Window.blit(textsurface,(100,130))
                    image = pygame.image.load('won.png')
                    Window.blit(image, (40,80))
                    pygame.display.update()
                    slide12 = myfont1.render('Congratulation', False, (0, 0, 0))
                    Window.blit(slide12,(125,210))
                    slide12 = myfont1.render('Do You Get', False, (0, 0, 0))
                    Window.blit(slide12,(150,260))
                    
                    ab8=str(round(re,2))
                    slide12 = myfont1.render(ab8, False, (0, 0, 0))
                    Window.blit(slide12,(170,310))
                    pygame.display.update()
                if(r1==11 and l1==0):
                    Window.fill((255,255,255))
                    options()
                    slide1l = myfont.render('Yes', False, (0, 0, 0))
                    Window.blit(slide1l,(30,440))
                    slide1r = myfont.render('No', False, (0, 0, 0))
                    Window.blit(slide1r,(435,440))

                    slide12 = myfont1.render("Do you want to play again ?", False, (0, 0, 0))
                    Window.blit(slide12,(5,200))
                    pygame.display.update()
                    mouse_position =(0,0)
                    f=0
                    while(True):
                        for even in pygame.event.get():
                            if ( even.type == pygame.MOUSEBUTTONUP ):
                                mouse_position = pygame.mouse.get_pos()
                                if RectangleObjects[1].collidepoint(mouse_position):
                                    pygame.quit()
                                    sys.exit()
                                elif RectangleObjects[0].collidepoint(mouse_position):
                                    r1,l1=0,11
                                    global r,l
                                    r,l=0,11
                                    f=1
                                    break
                        if(f==1):
                            break
                    
            if(r1==0 and l1==11):
                y=1
                while(y%2!=0):
                    y=random.randint(1,9)
                z=y
                x=1
                while(x%2!=0):
                    x=random.randint(1,50)
                m=x
                n=random.randint(2,10)
                o=random.randint(0,100)
                p=random.randint(0,100)
                q=random.randint(2,10)
                re=((((m/z)*n)+o)-p)*q
                Window.fill((255,255,255))
                options()
                slide1l = myfont.render('Start', False, (0, 0, 0))
                Window.blit(slide1l,(25,440))
                slide1r = myfont.render('Start', False, (0, 0, 0))
                Window.blit(slide1r,(425,440))
                image = pygame.image.load('a.png')
                Window.blit(image, (20, 20))
                pygame.display.update()
                r1,l1=-1,-1

if __name__=="__main__":
    main()
