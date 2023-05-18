import math

import pygame.draw

from pygame.math import Vector2
from utils.settings import readSettings


class GameObject:
    def __init__(self, position, velocity):
        self.angle = 0
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.settings = readSettings()
        img = pygame.image.load("assets/ship.svg")
        self.img = pygame.transform.scale_by(img, 0.4)
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.surface = pygame.transform.rotate(self.img, self.angle)
        self.rectangle = self.surface.get_rect(center=(self.position[0], self.position[1]))

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
        if self.handleCollisionLeft():
            self.rectangle.move_ip(self.settings['width'], 0)
        if self.handleCollisionRight():
            self.rectangle.move_ip(-self.settings['width'], 0)
        if self.handleCollisionTop():
            self.rectangle.move_ip(0, self.settings['height'])
        if self.handleCollisionDown():
            self.rectangle.move_ip(0, -self.settings['height'])


    # def collides_with(self, other_obj):
    #     distance = self.position.distance_to(other_obj.position)
    #     return distance < self.radius + other_obj.radius
