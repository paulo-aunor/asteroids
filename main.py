import pygame
import sys
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_fields = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.checkCollision(player):
                print("Game Over!!")
                sys.exit()
            
            for shot in shots:
                if asteroid.checkCollision(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
