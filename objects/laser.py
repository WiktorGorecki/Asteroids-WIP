import pygame

from objects.object import GameObject

class Laser (GameObject):
    def __int__(self, position, velocity):
        print("Debug: Creating new Laser object")
        GameObject.__init__(self, position, velocity)
