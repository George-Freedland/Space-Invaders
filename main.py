import pygame
from pygame import mixer

import random
import math

from Player import Player
from Laser import Laser
from Enemy import Enemy
from Score import Score
from GameOver import GameOver
 
def main():
    pygame.init()
    logo = pygame.image.load('images/enemy.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Space Invaders")
    screen = pygame.display.set_mode((800, 600))

    # Background Image
    background = pygame.image.load('images/background.jpg')

    # Background Music
    mixer.music.load('sounds/background.mp3')
    mixer.music.play(-1)
     
    # Player
    player = Player()

    # Enemies
    numOfEnemies = 6
    enemies = []
    for i in range(numOfEnemies):
        enemies.append(Enemy())
    
     # Laser
    laser = Laser()

    # Score
    score = Score()

    # Game Over
    gameOver = GameOver()
    
    # Collision Check
    def isCollision(enemyX, enemyY, laserX, laserY):
        distance = math.sqrt(math.pow(enemyX-laserX,2) + math.pow(enemyY-laserY,2))
        if distance < 64: 
            return True
        return False
    
    # Game Loop
    running = True 
    while running:
        screen.fill((0, 220, 235))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.setSpeed(2)
                if event.key == pygame.K_LEFT:
                    player.setSpeed(-2)
                if event.key == pygame.K_SPACE and laser.getState() == 'WAIT':
                    laserSound = mixer.Sound('sounds/laser.wav')
                    laserSound.play()
                    laser.setState('FIRE')
                    laser.setX(player.getX())
                    laser.fireLaser(screen)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.setSpeed(0)
                if event.key == pygame.K_RIGHT:
                    player.setSpeed(0)
        

        # Player Movement
        player.move()

        # Enemy Movement
        for i in range(numOfEnemies):
            # Game Over
            if enemies[i].getY() > 440:
                for j in range(numOfEnemies):
                    enemies[j].setY(2000)
                gameOver.show(screen)
                break

            enemies[i].move()
            
            
        # Laser Movement
        laser.move(screen)
        
        # Collision
        for i in range(numOfEnemies):
            collision = isCollision(enemies[i].getX(), enemies[i].getY(), laser.getX(), laser.getY())
            if collision and laser.getState() is 'FIRE':
                explosionSound = mixer.Sound('sounds/explosion.wav')
                explosionSound.play()
                laser.setY(480)
                laser.setState('WAIT')
                score.setValue(score.getValue() + 1)
                enemies[i].setX(random.randint(0, 770))
                enemies[i].setY(random.randint(50, 150)) 

        player.show(screen)
        for i in range(numOfEnemies):
            enemies[i].show(screen)
        score.show(screen)
        pygame.display.update()
     
if __name__=="__main__":
    main()
