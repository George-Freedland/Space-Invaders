import pygame

class GameOver:

    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 64)
        self.x = 200
        self.y = 250

    def show(self, screen):
        gameOver = self.font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(gameOver, (self.x, self.y))