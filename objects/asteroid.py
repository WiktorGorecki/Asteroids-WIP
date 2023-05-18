import math
from random import random, randrange

import pygame

from objects.object import GameObject


class Asteroid(GameObject):

    def __init__(self, position, velocity, img):
        print("Debug: Creating new Spaceship object")
        GameObject.__init__(self, position, velocity, pygame.transform.scale_by(img, 0.3))
        self.dir = randrange(0, 360) * math.pi / 180

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rectangle, width=5)
        screen.blit(self.surface, self.rectangle)

    def turn(self, angle):
        self.angle += angle
        self.surface = pygame.transform.rotate(self.img, self.angle)
        self.rectangle = self.surface.get_rect(center=self.position)

    def move(self):
        self.handleTeleportation()
        # self.turn(0.1)

        dx = self.velocity[0] * math.cos(self.dir)
        dy = self.velocity[1] * math.sin(self.dir)
        self.rectangle.move_ip(dx, dy)
        self.position = self.rectangle.center


#Don't run this my brother, unless you're crazy drunk
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

    # def move(self):
        # 

