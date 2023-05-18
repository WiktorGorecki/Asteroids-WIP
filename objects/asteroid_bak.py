import math
from random import random, randint

import pygame

from objects.object import GameObject

class Asteroid(GameObject):
    def __int__(self, postition, velocity, img):
        position = (randint(0, self.settings['width']), randint(0, self.settings['height']))
        print("Debug: Creating new Asteroid object")
        # GameObject.__init__(self, position, random.uniform(1, (40 - self.size) * 4 / 15), pygame.transform.scale_by(img, 0.2))
        # GameObject.__init__(self, position, velocity, pygame.transform.scale_by(img, 0.2))
        GameObject.__init__(self, position, velocity, pygame.transform.scale_by(img, 0.2))
        # GameObject.__init__(self, position, velocity, pygame.transform.scale_by(img, 0.2))
        # self.width = 5
        self.height = 5
        self.dir = random.randrange(0, 360) * math.pi / 180


    def draw(self, surface):
        pygame.draw.rect(surface, "white", self.rectangle, width=5)
        surface.blit(self.surface, self.rectangle)

    def move(self):
        self.position[0] += self.velocity * math.cos(self.dir)
        self.position[1] += self.velocity * math.sin(self.dir)