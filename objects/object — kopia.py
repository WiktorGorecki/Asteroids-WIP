import math

import pygame.draw
from pygame.math import Vector2
from utils.settings import readSettings

class GameObject:
    def __init__(self, position, velocity):
        self.angle = 50
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.settings = readSettings()
        self.img = pygame.image.load("assets/ship.svg")
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect(center=(self.position[0], self.position[1]))
        # self.rotatedRect = self.rotatedSurf.get_rect()
        # self.rotatedRect.center = (self.position[0], self.position[1])
        self.cos = math.cos(math.radians((self.angle+90)))
        self.sin = math.sin(math.radians((self.angle+90)))

        # self.settings = {
        #     "width": 1280,
        #     "height": 720,
        #     "fullscreen": False
        #     }

    def draw(self, surface):
        pass

    def move(self):
        # print("help")
        self.handleTeleportation()

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

    # def collides_with(self, other_obj):
    #     distance = self.position.distance_to(other_obj.position)
    #     return distance < self.radius + other_obj.radius