import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    # Split the asteroid into two smaller asteroids
    def split(self):
        self.kill()

        # If the asteroid is too small, don't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Generate a random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)
        
        # Create two new asteroids
        a = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        b = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

        # Set their velocities
        a.velocity = self.velocity.rotate(+angle) * 1.2
        b.velocity = self.velocity.rotate(-angle) * 1.2

        
