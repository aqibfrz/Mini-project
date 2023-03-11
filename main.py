import pygame
from ball import Ball
from player import Player

RED = (255, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 220)
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


def game_loop():
    running = True
    player1 = Player(0, display.get_height() - 50, 2.2, display)
    player1.moveToHorizontalCenter()
    player2 = Player(0, 10, 2.2, display)
    player2.moveToHorizontalCenter()
    ballX = player1.x + (player1.image.get_width() / 2)
    ball = Ball(ballX, player1.y, 2.5, display)

    while running:
        if player1.life == 0:
            display.fill(BLACK)
            screen_score("The Winner is PLAYER 1. Press ENTER.", WHITE, final_display_x, final_display_y - 50, font2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                player1.resetScore()
                player1.resetLife()
                player2.resetScore()
                player2.resetLife()
                game_loop()
        elif player2.life == 0:
            display.fill(BLACK)
            screen_score("The Winner is PLAYER 2. Press ENTER.", WHITE, final_display_x, final_display_y - 50, font2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                player1.resetScore()
                player1.resetLife()
                player2.resetScore()
                player2.resetLife()
                game_loop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

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

            # Draw players and ball
            player1.draw()
            player2.draw()

            screen_score("Player 2 score: " + str(player2.score), RED, 15, 15, font1)  # + "
            screen_score("Player 1 score: " + str(player1.score), RED, 15, display.get_height() - 35, font1)
            screen_score("life: " + str(player2.life), RED, (display.get_width() - 15) - chance_width, 15, font1)
            screen_score("life: " + str(player1.life), RED, (display.get_width() - 15) - chance_width, display.get_height() - 35,
                         font1)
            ball.update(player1, player2)
        pygame.display.update()

    pygame.quit()
    quit()


run = True
while run:
    a = pygame.transform.scale(welcome, (1300, 660))
    display.blit(a, (0, 0))
    screen_score("Player 1", WHITE, display.get_width() / 22, display.get_height() / 5.65, font2)
    screen_score("Player 2", WHITE, display.get_width() / 1.447, display.get_height() / 1.297, font2)
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
