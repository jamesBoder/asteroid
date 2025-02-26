# this allows us to use code from 
# the open-source pygame library
# throughout this file
import pygame
from constants import *

# Initialize game
pygame.init()

# Display Screen
screen = pygame.display.set_mode((1280, 800))
pygame.display.set_caption("My Pygame Window")
                                 
black = (0, 0, 0)

def main():
    print("Starting Asteroids!")

if __name__ == "__main__":
    main()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.Surface.fill( screen, black)
    pygame.display.flip()