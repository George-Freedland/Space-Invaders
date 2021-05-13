import pygame

class Score:

    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.x = 10
        self.y = 10
    
    def show(self, screen):
        score = self.font.render("Score: " + str(self.value), True, (255, 255, 255))
        screen.blit(score, (self.x, self.y))

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value