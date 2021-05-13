import pygame

class Laser:

    def __init__(self):
        self.x = 0 
        self.y = 480
        self.speed = 2
        self.state = 'WAIT'
        self.img = pygame.image.load('images/laser.png')
    
    def fireLaser(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def move(self, screen):
        if self.state == 'FIRE':
            self.fireLaser(screen)
            self.y -= self.speed

        if self.y <= 0:
            self.state = 'WAIT'
            self.y = 480

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