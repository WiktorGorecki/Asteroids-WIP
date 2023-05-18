import math

import pygame

from objects.object import GameObject


class Spaceship(GameObject):
    def __init__(self, position, velocity):
        GameObject.__init__(self, position, velocity)
        self.keyUp = pygame.K_UP
        self.keyDown = pygame.K_DOWN
        self.keyLeft = pygame.K_LEFT
        self.keyRight = pygame.K_RIGHT

    def draw(self, surface):
        surface.blit(self.rotatedSurf, self.rotatedRect)
        # surface.blit(self.img, (0,0))
        # blit_position = self.position - Vector2(self.radius)
        # surface.blit(self.sprite, blit_position)
        # pygame.draw.rect(surface, "green", pygame.Rect(self.position[0], self.position[1], self.height, self.width))
        # pygame.draw.rect(surface, "green", self.position)

    def turnLeft(self):
        self.angle += 0.5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect(center=(self.position[0], self.position[1]))
        # self.rotateSurf = pygame.transform.rotate(self.img, self.angle)
        # self.rotateRect = self.rotateSurf.get_rect()
        # self.rotatedRect.center = (self.position[0], self.position[1])
        # self.cos = math.cos(math.radians(self.angle+90))
        # self.sin = math.sin(math.radians(self.angle + 90))

    def move(self, keys):
        # super().move()

        # if keys[self.keyUp]:
            # self.position[1] -= self.sin * self.velocity[1]
            # self.position[0] += self.cos * self.velocity[0]
            # self.position[1] -= self.sin * self.velocity[1]
            # self.position[0] += self.cos * self.velocity[0]
        if keys[self.keyLeft]:
            self.turnLeft()

        if keys[self.keyUp]:
            self.rotatedRect = self.rotatedRect.move(self.cos *4, self.sin *  4)
            # self.position[1] -= self.velocity[1]
            print(self.position)
        # elif keys[self.keyDown]:
        #     self.position[1] += self.velocity[1]
        # elif keys[self.keyLeft]:
        #     self.position[0] -= self.velocity[0]
        # elif keys[self.keyRight]:
        #     self.position[0] += self.velocity[0]
