import random
import pygame

from player import Player


class Ball:
    def __init__(self, xPosition: int, yPosition: int, speed: float, screen: pygame.Surface) -> None:
        self.x = xPosition  # self.x is the top left corner's x position of the image
        self.y = yPosition  # self.y is the top left corner's y position of the image
        self.speed = speed
        self.screen = screen
        self.image = pygame.image.load('ping-pong.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.whoHasBall = 'PLAYER1'
        list1 = [1, 2, 3]
        r1 = random.choice(list1)
        if r1 == 1:
            self.moveDirection = 'UP'
        elif r1 == 2:
            self.moveDirection = 'UP-LEFT'
        elif r1 == 3:
            self.moveDirection = 'UP-RIGHT'
        self.isMoving = False

    def moveLeft(self):
        self.x = self.x - self.speed
        # Detect collision with screen left
        if self.x < 0:
            self.x = 0
            if self.moveDirection == 'UP-LEFT':
                self.moveDirection = 'UP-RIGHT'
            elif self.moveDirection == 'DOWN-LEFT':
                self.moveDirection = 'DOWN-RIGHT'

    def moveRight(self):
        self.x = self.x + self.speed
        # Detect collision with screen right
        if self.x > (self.screen.get_width() - self.image.get_width()):
            self.x = self.screen.get_width() - self.image.get_width()
            if self.moveDirection == 'UP-RIGHT':
                self.moveDirection = 'UP-LEFT'
            elif self.moveDirection == 'DOWN-RIGHT':
                self.moveDirection = 'DOWN-LEFT'

    def moveUp(self, player1: Player, player2: Player):
        self.y = self.y - self.speed
        # Detect collision with screen up
        if self.y < 0:
            player2.decreaseLife()
            player1.increaseScore()
            player1.increaseScore()
            self.whoHasBall = 'PLAYER2'
            self.isMoving = False

    def moveDown(self, player1: Player, player2: Player):
        self.y = self.y + self.speed
        # Detect collision with screen down
        if self.y > (self.screen.get_height() - self.image.get_height()):
            player1.decreaseLife()
            player2.increaseScore()
            player2.increaseScore()
            self.whoHasBall = 'PLAYER1'
            self.isMoving = False

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def update(self, player1: Player, player2: Player):
        if self.isMoving:
            if self.moveDirection == 'UP':
                self.moveUp(player1, player2)
            elif self.moveDirection == 'DOWN':
                self.moveDown(player1, player2)
            elif self.moveDirection == 'UP-RIGHT':
                self.moveUp(player1, player2)
                self.moveRight()
            elif self.moveDirection == 'DOWN-RIGHT':
                self.moveDown(player1, player2)
                self.moveRight()
            elif self.moveDirection == 'UP-LEFT':
                self.moveUp(player1, player2)
                self.moveLeft()
            elif self.moveDirection == 'DOWN-LEFT':
                self.moveDown(player1, player2)
                self.moveLeft()

            if (self.y >= player2.y and self.y <= player2.y + player2.image.get_height()) \
                    and (self.x >= player2.x and self.x <= player2.x + player2.image.get_width()):
                player2.increaseScore()
                if self.moveDirection == 'UP':
                    list1 = [1, 2, 3]
                    r1 = random.choice(list1)
                    if r1 == 1:
                        self.moveDirection = 'DOWN'
                    elif r1 == 2:
                        self.moveDirection = 'DOWN-LEFT'
                    elif r1 == 3:
                        self.moveDirection = 'DOWN-RIGHT'
                else:
                    self.moveDirection = 'DOWN'
            elif (self.y >= player1.y and self.y <= player1.y + player1.image.get_height()) \
                    and (self.x >= player1.x and self.x <= player1.x + player1.image.get_width()):
                player1.increaseScore()
                if self.moveDirection == 'DOWN':
                    list1 = [1, 2, 3]
                    r1 = random.choice(list1)
                    if r1 == 1:
                        self.moveDirection = 'UP'
                    elif r1 == 2:
                        self.moveDirection = 'UP-LEFT'
                    elif r1 == 3:
                        self.moveDirection = 'UP-RIGHT'
                else:
                    self.moveDirection = 'UP'

        else:
            if self.whoHasBall == 'PLAYER1':
                self.moveDirection = 'UP'
                self.x = player1.x + ((player1.image.get_width() / 2) - (self.image.get_width() / 2))
                self.y = player1.y - self.image.get_height()
            else:
                self.moveDirection = 'DOWN'
                self.x = player2.x + ((player1.image.get_width() / 2) - (self.image.get_width() / 2))
                self.y = player2.y + self.image.get_height() + 5

        self.draw()
