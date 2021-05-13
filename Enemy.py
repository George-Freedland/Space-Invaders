import pygame
import random

class Enemy:

    def __init__(self):
        self.x = random.randint(0, 770)
        self.y = random.randint(50, 150)
        self.speedX = 1
        self.img = pygame.image.load('images/enemy.png')
    
    def fireLaser(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.x += self.speedX
        if self.x >= 770 or self.x <= 0:
            self.speedX *= -1
            self.y += 40
        
    def show(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def getX(self):
        return self.x
    def setX(self, x):
        self.x = x
    def getY(self):
        return self.y
    def setY(self, y):
        self.y = y
    def getSpeed(self):
        return self.speed
    def setSpeed(self, speed):
        self.speed = speed
    def getState(self):
        return self.state
    def setState(self, state):
        self.state = state
    def getImg(self):
        return self.img
    def setImg(self, img):
        self.img = img