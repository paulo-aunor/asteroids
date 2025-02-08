import pygame
from constants import *

def main():
    game_run = True
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while (game_run == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("0,0,0")

if __name__ == "__main__":
    main()
