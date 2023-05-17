import pygame

from objects.object import GameObject

class Asteroid(GameObject):
    def __int__(self, position, velocity):
        GameObject.__init__(self, position, velocity)
        #TODO: Add angle randomisation

    def draw(self, surface):
        pygame.draw.rect(surface, "green", pygame.Rect(self.position[0], self.position[1], self.height, self.width))
