import pygame

#initializing pygame
pygame.init()


#creating a screen.
display=pygame.display.set_mode((800,600))
pygame.display.update()

#background
background=pygame.image.load('3748275_75291.png')


#title and icon.
pygame.display.set_caption("ping pong")
icon=pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)


#player1.
playerImg=pygame.image.load('delete (2).png')
playerX=370
playerY=480
playerX_change=0
def player1(x,y):
    display.blit(playerImg,(x,y))


#player2.
playerImg2=pygame.image.load('delete (2).png')
playerA=299
playerB=9
playerA_change=0
def player2(a,b):
    display.blit(playerImg2,(a,b))

    
# game infinite loop.
running=True
while running:
    #RGB red ,blue ,green.
    display.fill((0,0,0))
    display.blit(background,(-100,-100))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        #if key stroke is pressed weither it is right or left.
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-0.3
            if event.key==pygame.K_RIGHT:
                playerX_change=0.3
            if event.key==pygame.K_a:
                playerA_change=-0.3
            if event.key==pygame.K_d:
                playerA_change=0.3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0  
            if event.key==pygame.K_a or event.key==pygame.K_j:
                playerA_change=0 
    playerX += playerX_change
    playerA += playerA_change

    if playerX <=0:
        playerX=0
    elif playerX >=671:
        playerX=671   

    
    if playerA<=0:
        playerA=0
    elif playerA>=671:
        playerA=671 
    
    
    player1(playerX,playerY)
    player2(playerA,playerB)

    pygame.display.update()

pygame.quit()
          

 




