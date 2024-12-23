#!/usr/bin/env python3

from constants import *    
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
import pygame
import sys


updatable = pygame.sprite.Group()
drowable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Shot.containers = (updatable, drowable, shots)
Player.containers = (updatable, drowable)
Asteroid.containers = (updatable, drowable, asteroids) 
AsteroidField.containers = (updatable,)


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    playr = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    af = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for u in updatable:
            u.update(dt)
        
        for a in asteroids:
            for s in shots:
                if a.collides(s):
                    a.split(); s.kill()
                    
            if playr.collides(a):
                 print("YOU DIED")
                 sys.exit(0)

        screen.fill(color="Black")
        for d in drowable:
            d.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()

