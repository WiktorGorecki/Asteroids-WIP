import pygame

from objects.object import GameObject

class Asteroid(GameObject):
    def __int__(self, position, velocity):
        print("Debug: Creating new Asteroid object")
        GameObject.__init__(self, position, velocity)
        self.width = 5
        self.height = 5
        #TODO: Add angle randomisation

    def draw(self, surface):
        pygame.draw.rect(surface, "green", pygame.Rect(self.position[0], self.position[1], self.height, self.width))

    # def move(self):
        # 