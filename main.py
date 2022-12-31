import pygame

from ball import Ball
from player import Player

red = (255, 255, 255)
white = (255, 0, 0)

# initializing pygame
pygame.init()
font = pygame.font.SysFont(None, 55)

# creating a screen.
display = pygame.display.set_mode((1280, 660))

# background
background = pygame.image.load('b2.jpg')


# title and icon.
pygame.display.set_caption("ping pong")
icon = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)

player1 = Player(0, display.get_height() - 50, 2.2, display)
player1.moveToHorizontalCenter()
player2 = Player(0, 10, 2.2, display)
player2.moveToHorizontalCenter()
ballX = player1.x + (player1.image.get_width() / 2)
ball = Ball(ballX, player1.y, 0.9, display)

font = pygame.font.SysFont(None, 55)
def screen_score(text, color, x, y):
    screen_score = font.render(text, True, color)
    display.blit(screen_score, [x, y])



# game infinite loop.

def game_loop():
    running = True
    # ball.isMoving = True

    with open("highest.txt", "r") as f:
        highest = f.read()
    score = 0
    while running:
        # if
        # if score > highest:
        #     highest = score
        #     with open("hiscore.txt", "w") as f:
        #         f.write(str(highest))
        #     display.fill(red)
            # screen_score("game over! please enter to restart", white, 350, 270)
        #     pygame.display.update()
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             running = False
        #     key = pygame.key/.get_pressed()
        #     if key[pygame.K_RETURN]:
        #         ball.isMoving = True
        #         game_loop()

        # else:
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
            newImage = pygame.transform.scale(background, (1300, 650))
            display.blit(newImage, (0, 0))
            # pygame.display.flip()



    # Draw players and ball
            player1.draw()

            screen_score("Player 2 score: " + str(player2.score) + "                                                                                    high score: " + str(highest), red, 15, 1)
            screen_score("Player 1 score: " + str(player1.score) + "                                                                                    high score: " + str(highest), red, 15, display.get_height() - 40)
            player2.draw()
            ball.update(player1, player2)
            pygame.display.update()

    pygame.quit()
    quit()
game_loop()
