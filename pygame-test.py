import pygame

class Player:
    def __init__(self, xPosition, yPosition, speed) -> None:
        self.x = xPosition # self.x is the top left corner's x position of the image
        self.y = yPosition # self.y is the top left corner's y position of the image
        self.speed = speed
        self.image = pygame.image.load('player.png')

    def draw(self):
        display.blit(self.image, (self.x, self.y))

    def moveLeft(self):
        self.x = self.x - self.speed
        if self.x < 0: # Detect collision with screen left
            self.x = 0

    def moveRight(self):
        self.x = self.x + self.speed
        if self.x > (display.get_width() - self.image.get_width()): # Detect collision with screen right
            self.x = display.get_width() - self.image.get_width()

    def moveToHorizontalCenter(self):
        centerX = (int)((display.get_width() / 2) - (self.image.get_width() / 2))
        self.x = centerX


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

player1 = Player(0, 480, 3.0)
player1.moveToHorizontalCenter()
player2 = Player(0, 9, 3.0)
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