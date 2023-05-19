import math
from random import random, randrange, randint
from pygame.math import Vector2

import pygame

from objects.object import GameObject


class Asteroid(GameObject):

    def __init__(self, position, velocity, img):
        print("Debug: Creating new Spaceship object")
        self.health = 3
        GameObject.__init__(self, position, Vector2(velocity).rotate(randint(0, 360)), pygame.transform.scale_by(img, 0.1), angle=randint(0, 360))
        # self.dir = randrange(0, 360) * math.pi / 180

    def draw(self, screen):
        # pygame.draw.rect(screen, "white", pygame.Rect(self.position, (self.width, self.height)), width=5)
        # pygame.draw.rect(screen, "white", self.surface.get_rect(topleft=(self.position[0], self.position[1])), width=5)
        pygame.draw.rect(screen, "white", self.rectangle, width=2)
        screen.blit(self.surface, self.position)

    def turn(self, angle):
        self.angle += angle
        self.surface = pygame.transform.rotate(self.img, self.angle)
        self.rectangle = self.surface.get_rect(topleft=self.position)
        self.velocity.rotate_ip(-angle)

    def move(self):
        self.handleTeleportation()

        self.position += self.velocity
        self.rectangle = self.surface.get_rect(topleft=self.position)
        # self.turn(0.1)

    def checkDestroy(self):
        if self.health == 0:
            return True
        else:
            return False


class AsteroidSmall(Asteroid):
    def __init__(self, position, velocity, img):
        print("Debug: Creating new Spaceship object")
        GameObject.__init__(self, position, velocity, pygame.transform.scale_by(img, 0.3))
        self.dir = randrange(0, 360) * math.pi / 180

    def __int__(self, position, velocity):
        print("Debug: Creating new Asteroid object")
        GameObject.__init__(self, position, velocity)
        self.width = 30
        self.height = 30
        #TODO: Add angle randomisation

    def draw(self, surface):
        pygame.draw.rect(surface, "green", pygame.Rect(self.position[0], self.position[1], self.height, self.width))


