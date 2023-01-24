import pygame

class single1:
    def __init__(self, xPosition:int, yPosition:int, speed : float, screen:pygame.Surface) -> None:
        self.x = xPosition  # self.x is the top left corner's x position of the image
        self.y = yPosition  # self.y is the top left corner's y position of the image
        self.speed = speed + 2.5
        self.screen = screen
        self.image = pygame.image.load('player.png')
        self.score = 0
        self.image = pygame.transform.scale(self.image, (1700, 10))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))