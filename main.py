import pygame
from ball import Ball
from player import Player

WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)
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
welcome = pygame.image.load('welcome.jpg')

# title and icon.
pygame.display.set_caption("Ping Pong Game")
icon = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)


def display_text(text, color, x, y, z):
    font = pygame.font.SysFont(None, z)
    t = font.render(text, True, color)
    display.blit(t, [x, y])


def game_loop():
    running = True
    player1 = Player(0, display.get_height() - 50, 4.6, display)
    player1.moveToHorizontalCenter()
    player2 = Player(0, 10, 4.6, display)
    player2.moveToHorizontalCenter()
    ballX = player1.x + (player1.image.get_width() / 2)
    ball = Ball(ballX, player1.y, 5, display)

    while running:
        if player1.life == 0:
            a = pygame.transform.scale(background, (1300, 660))
            display.blit(a, (0, 0))
            display_text("The Winner is PLAYER 2. Press ENTER.", PURPLE, final_display_x, final_display_y - 50, font2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                player1.resetScore()
                player1.resetLife()
                player2.resetScore()
                player2.resetLife()
                welcome_loop()
        elif player2.life == 0:
            a = pygame.transform.scale(background, (1300, 660))
            display.blit(a, (0, 0))
            display_text("The Winner is PLAYER 1. Press ENTER.", PURPLE, final_display_x, final_display_y - 50, font2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                player1.resetScore()
                player1.resetLife()
                player2.resetScore()
                player2.resetLife()
                welcome_loop()
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

            display_text("Player 2 score: " + str(player2.score), WHITE, 15, 15, font1)
            display_text("Player 1 score: " + str(player1.score), WHITE, 15, display.get_height() - 35, font1)
            display_text("life: " + str(player2.life), WHITE, (display.get_width() - 15) - chance_width, 15, font1)
            display_text("life: " + str(player1.life), WHITE, (display.get_width() - 15) - chance_width,
                         display.get_height() - 35, font1)
            ball.update(player1, player2)
        pygame.display.update()

    pygame.quit()
    quit()


def welcome_loop():
    run = True
    while run:
        a = pygame.transform.scale(welcome, (1300, 660))
        display.blit(a, (0, 0))
        display_text("PLAYER 1", PURPLE, 80, (display.get_height() / 2) - 50, font2)
        display_text("PLAYER 2", PURPLE, display.get_width() - 320, (display.get_height() / 2) - 50, font2)
        display_text("ENTER TO START THE GAME", PURPLE, 50, display.get_height() - 50, font1)
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


welcome_loop()
