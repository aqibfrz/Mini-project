import pygame
from player import Player


# initializing pygame
pygame.init()

# creating a screen.
display = pygame.display.set_mode((800, 600))
pygame.display.update()

# background
background = pygame.image.load('background.png')


# title and icon.
pygame.display.set_caption("ping pong")
icon = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)

player1 = Player(0, 480, 3.0, display)
player1.moveToHorizontalCenter()
player2 = Player(0, 9, 3.0, display)
player2.moveToHorizontalCenter()

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

    # Draw background
    display.fill((0, 0, 0)) # RGB red ,blue ,green.
    display.blit(background, (-100, -100))

    # Draw players
    player1.draw()
    player2.draw()

    pygame.display.update()

pygame.quit()