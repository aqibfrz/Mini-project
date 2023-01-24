import pygame

from ball import Ball
from player import Player
from single import single1

# name1 = input("Enter player1 name: ")
# name2 = input("Enter  player2 name: ")
name1 = "player 1"
name2 = "player 2"

red = (255, 255, 255)
black = (0, 0, 0)
white = (255, 255, 220)
final_display_x = 180
final_display_y = 300
chance_width = 120
# initializing pygame
pygame.init()
font2 = 70
font1 = 35
# creating a screen.
display = pygame.display.set_mode((1280, 660))

# background
background = pygame.image.load('background.jpg')
welcome = pygame.image.load('bag1.jpg')



# title and icon.
pygame.display.set_caption("ping pong")
icon = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)


def screen_score(text, color, x, y, z):
    font = pygame.font.SysFont(None, z)
    screen_score = font.render(text, True, color)
    display.blit(screen_score, [x, y])
#
# def screen_score1(text, color, x, y):
#     screen_score = font1.render(text, True, color)
#     display.blit(screen_score, [x, y])

# game infinite loop.

def game_loop():
    running = True
    # ball.isMoving = True
    n = 0
    nk=0
    s = 0
    i = 5
    j = 5
    player1 = Player(0, display.get_height() - 50, 2.2, display)
    player1.moveToHorizontalCenter()
    player2 = Player(0, 10, 2.2, display)
    player2.moveToHorizontalCenter()
    ballX = player1.x + (player1.image.get_width() / 2)
    ball = Ball(ballX, player1.y, 2.5, display)

    with open("highest.txt", "r") as f:
        highest = f.read()
    # with open("hiscore.txt", "r") as f:
    #     hiscore = f.read()
    # score = 0
    # chance = 5
    # highest = 0
    # hiscore = 0

    while running:
        # if s == 0:
        #     welcome()
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             running = False
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_RETURN:
        #                 s += 1
        #                 game_loop()


            # if player2.score > int(highest):
            #     highest = player2.score
            # with open("highest.txt", "w") as f:
            #     f.write(str(highest))
            # if player1.score > int(hiscore):
            #     hiscore = player1.score
            # with open("hiscore.txt", "w") as f:

        # else:    #     f.write(str(hiscore))
            if player1.score > n:
                n+=10
                i = i-1
            if player2.score > nk:
                    nk += 10
                    j = j-1
            if i == 0:
               display.fill(black)
               screen_score("THE WINNER IS " + name1.upper(), white, final_display_x , final_display_y - 50, font2)
               # screen_score(name1.upper(), white, final_display_x - 40, final_display_y + 50)
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
               key = pygame.key.get_pressed()
               if key[pygame.K_RETURN]:
                   player1.score = 0
                   player2.score = 0
                   game_loop()
            elif j == 0:
               display.fill(black)
               screen_score("THE WINNER IS " + name2.upper(), white, final_display_x , final_display_y - 50, font2)
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
               key = pygame.key.get_pressed()
               if key[pygame.K_RETURN]:
                   player1.score = 0
                   player2.score = 0
                   game_loop()

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                # Key handler
                # using `pygame.key.get_pressed()` to get continuous motion
                keys = pygame.key.get_pressed()

                if keys[pygame.K_RETURN] or keys[pygame.K_SPACE] and not ball.isMoving:
                    ball.isMoving = True
                if keys[pygame.K_LEFT]:
                    player1.moveLeft()
                if keys[pygame.K_RIGHT]:
                    player1.moveRight()
                if keys[pygame.K_a]:
                    player2.moveLeft()
                if keys[pygame.K_d]:
                    player2.moveRight()


                # Draw background
                newImage = pygame.transform.scale(background, (1300, 660))
                display.blit(newImage, (0, 0))
                # pygame.display.flip()



        # Draw players and ball
                player1.draw()
                player2.draw()

                screen_score(name2 + " " + "score: " + str(player2.score), red, 15, 15, font1) #+ "
                screen_score(name1 + " " + "score: " + str(player1.score), red, 15, display.get_height() - 35, font1) #+ "                                                                     high score: " + str(highest), red, 15, display.get_height() - 40)
                screen_score("chance: " + str(i), red, (display.get_width() - 15) - chance_width, 15, font1)
                screen_score("chance: " + str(j), red, (display.get_width() - 15) - chance_width, display.get_height() - 35, font1)
                ball.update(player1, player2)
            pygame.display.update()

    pygame.quit()
    quit()

# game_loop()
run = True
while run:
    # display.fill(black)
    a = pygame.transform.scale(welcome, (1300, 660))
    display.blit(a, (0, 0))
    # screen_score("WELCOME TO GAME", white, display.get_width()/4.2, display.get_height()/13, font2)
    # screen_score("&", white, display.get_width()/2.3, display.get_height()/2.05, font2+20)
    # screen_score("ENTER TO STAR GAME", white, display.get_width()/2.8, display.get_height()/1.1, font2 - 50)
    screen_score(name1.upper(), white, display.get_width()/22, display.get_height()/5.65, font2)
    screen_score(name2.upper(), white, display.get_width()/1.447, display.get_height()/1.297, font2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            run = False
            game_loop()
    pygame.display.update()
pygame.quit()
quit()
