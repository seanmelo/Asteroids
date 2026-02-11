import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen, color="white"):
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        vector_a = self.velocity.rotate(angle)
        vector_b = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = vector_a * 1.2
        asteroid_b.velocity = vector_b * 1.2
