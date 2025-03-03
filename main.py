# this allows us to use code from 
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Initialize game
pygame.init()

# Display Screen
screen = pygame.display.set_mode((1280, 800))
pygame.display.set_caption("My Pygame Window")
black = (0, 0, 0)

# Delta Time
clock = pygame.time.Clock() # Create an instance of the Clock object
dt = 0 # Initialize delta time variable


# Groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

# Player
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)

# Add player to groups
Player.containers = updatable, drawable
player.add(updatable, drawable,)
Asteroid.containers = updatable, drawable, asteroids
AsteroidField.containers = (updatable,)
Shot.containers = (shots,)
 
asteroid_field = AsteroidField()


def main():
    print("Starting Asteroids!")
    

if __name__ == "__main__":
    main()
    

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.Surface.fill(screen, black)

    # Update everything
    updatable.update(dt)
    shots.update(dt) # update the shots

    # Draw everything
    for draws in drawable:
        draws.draw(screen)

    for shot in shots:
        shot.draw(screen)

    print(f'Number of shots: {len(shots)}')

    pygame.display.flip()

    for asteroid in asteroids:
        if player.collisionDetect(asteroid):
            print("Game Over!")
            running = False

    for asteroid in asteroids:
        for shot in shots:
            if shot.collisionDetect(asteroid):
                shot.kill()
                asteroid.split()
                print("Asteroid Shot!")

    dt = clock.tick(60) / 1000


    
    

