import pygame

from ball import Ball
from player import Player


# initializing pygame
pygame.init()

# creating a screen.
display = pygame.display.set_mode((600, 600))
pygame.display.update()

# background
background = pygame.image.load('background.png')


# title and icon.
pygame.display.set_caption("ping pong")
icon = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)

player1 = Player(0, display.get_height() - 60, 1.0, display)
player1.moveToHorizontalCenter()
player2 = Player(0, 50, 1.0, display)
player2.moveToHorizontalCenter()
ballX = player1.x + (player1.image.get_width()/2)
ball = Ball(ballX, player1.y, 0.5, display)

# game infinite loop.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handler
    # using `pygame.key.get_pressed()` to get continuous motion
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1.moveLeft()
    if keys[pygame.K_RIGHT]:
        player1.moveRight()
    if keys[pygame.K_a]:
        player2.moveLeft()
    if keys[pygame.K_d]:
        player2.moveRight()
    if keys[pygame.K_SPACE] and not ball.isMoving:
        ball.isMoving = True

    # Draw background
    display.fill((0, 0, 0))  # RGB red ,blue ,green.
    display.blit(background, (-100, -100))

    # Draw players and ball
    player1.draw()
    player2.draw()
    ball.update(player1, player2)

    pygame.display.update()

pygame.quit()
