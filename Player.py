import pygame

class Player:

    def __init__(self):
        self.x = 400 
        self.y = 500
        self.speed = 0
        self.img = pygame.image.load("images/player.png")
    
    def move(self):
        self.x += self.speed
        if self.x <= 0:
            self.x = 0
        elif self.x >= 770:
            self.x = 770

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
    def getImg(self):
        return self.img
    def setImg(self, img):
        self.img = img