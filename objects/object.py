import pygame.draw
from pygame.math import Vector2
from utils.settings import readSettings

class GameObject:
    def __init__(self, position, velocity):
        self.angle = 0
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.height = 40
        self.width = 40
        self.settings = readSettings()

    def draw(self, surface):
        pass

    def move(self):
        pass

    def handleCollisionLeft(self):
        return self.position[0] <= 0

    def handleCollisionRight(self):
        width = self.settings['width'];
        return self.self.position[0]+self.width >= width

    def handleCollisionDown(self):
        height = self.settings['height'];
        return self.self.position[1] + self.width >= height

    def handleCollisionTop(self):
        return self.position[1] <= 0

    # def collides_with(self, other_obj):
    #     distance = self.position.distance_to(other_obj.position)
    #     return distance < self.radius + other_obj.radius