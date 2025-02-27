# shot.py
import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity
    
    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt

        # Remove if off-screen
        if (self.position.x < -self.radius or 
            self.position.x > SCREEN_WIDTH + self.radius or
            self.position.y < -self.radius or
            self.position.y > SCREEN_HEIGHT + self.radius):
            self.kill()  # Remove from all groups
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.radius)

        print("Shot Drawn")