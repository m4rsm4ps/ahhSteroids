import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color="White",
            center=self.position,
            radius=self.radius,
            width=2
        )

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vel_one = self.velocity.rotate(angle)
        vel_two = self.velocity.rotate(-angle)
        new_aster_rad = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position[0], self.position[1], new_aster_rad)
        ast2 = Asteroid(self.position[0], self.position[1], new_aster_rad)
        ast1.velocity = vel_one * 1.2
        ast2.velocity = vel_two * 1.2


