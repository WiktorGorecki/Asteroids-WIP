import math

import pygame.draw

from pygame.math import Vector2
from utils.settings import readSettings
#
# class GameObject:
#     def __init__(self, position, velocity, img, angle=0):
#         self.angle = angle
#         self.position = Vector2(position)
#         self.velocity = Vector2(velocity)
#         self.settings = readSettings()
#         # self.img = pygame.transform.scale_by(img, 0.4)
#         self.img = img
#         self.width = self.img.get_width()
#         self.height = self.img.get_height()
#         self.surface = pygame.transform.rotate(self.img, self.angle)
#         self.rectangle = self.surface.get_rect(topleft=(self.position[0], self.position[1]))
#
#     def draw(self, surface):
#         pass
#
#     def move(self):
#         pass
#
#
#     def handleCollisionLeft(self):
#         return self.position[0] <= 0
#
#     def handleCollisionRight(self):
#         width = self.settings['width']
#         return self.position[0]+self.width >= width
#
#     def handleCollisionDown(self):
#         height = self.settings['height']
#         return self.position[1] + self.width >= height
#
#     def handleCollisionTop(self):
#         return self.position[1] <= 0
#
#     def handleTeleportation(self):
#         width = self.settings['width']
#         height = self.settings['height']
#         if self.handleCollisionLeft() or self.handleCollisionRight() or self.handleCollisionDown() or self.handleCollisionTop():
#             self.position[0] %= width
#             self.position[1] %= height
#
#     def collision(self, other):
#         # pygame.mixer.Sound.play(self.collision_sound)
#         return self.rectangle.colliderect(other.rectangle)


class GameObject:
    def __init__(self, position, velocity, img, angle=0):
        self.angle = angle
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.settings = readSettings()
        # self.img = pygame.transform.scale_by(img, 0.4)
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.surface = pygame.transform.rotate(self.img, self.angle)
        self.rectangle = self.surface.get_rect(topleft=(self.position[0], self.position[1]))

    def draw(self, surface):
        pass

    def move(self):
        pass


    def handleCollisionLeft(self):
        return self.position[0] <= 0

    def handleCollisionRight(self):
        width = self.settings['width']
        return self.position[0]+self.width >= width

    def handleCollisionDown(self):
        height = self.settings['height']
        return self.position[1] + self.width >= height

    def handleCollisionTop(self):
        return self.position[1] <= 0

    def handleTeleportation(self):
        width = self.settings['width']
        height = self.settings['height']
        if self.handleCollisionLeft() or self.handleCollisionRight() or self.handleCollisionDown() or self.handleCollisionTop():
            self.position[0] %= width
            self.position[1] %= height

    def collision(self, other):
        return self.rectangle.colliderect(other.rectangle)
