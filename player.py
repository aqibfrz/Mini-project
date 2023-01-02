import pygame

class Player:
    def __init__(self, xPosition:int, yPosition:int, speed : float, screen:pygame.Surface) -> None:
        self.x = xPosition  # self.x is the top left corner's x position of the image
        self.y = yPosition  # self.y is the top left corner's y position of the image
        self.speed = speed + 2
        self.screen = screen
        self.image = pygame.image.load('player.png')
        self.score = 0
        self.image = pygame.transform.scale(self.image, (200, 25))

    def increase(self):
        self.score += 10
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y+5))

    def moveLeft(self):
        self.x = self.x - self.speed
        if self.x < 0:  # Detect collision with screen left
            self.x = 0

    def moveRight(self):
        self.x = self.x + self.speed
        if self.x > (self.screen.get_width() - self.image.get_width()):  # Detect collision with screen right
            self.x = self.screen.get_width() - self.image.get_width()

    def moveToHorizontalCenter(self):
        centerX = (int)((self.screen.get_width() / 2) - (self.image.get_width() / 2))
        self.x = centerX
