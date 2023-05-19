import math

import pygame
from pygame.math import Vector2


from objects.object import GameObject
from utils.settings import readSettings

class Spaceship(GameObject):
    def __init__(self, position, velocity, img):
        print("Debug: Creating new Spaceship object")
        GameObject.__init__(self, position, Vector2(velocity).rotate(-135), pygame.transform.scale_by(img, 0.2))
        self.keyUp = pygame.K_UP
        self.keyDown = pygame.K_DOWN
        self.keyLeft = pygame.K_LEFT
        self.keyRight = pygame.K_RIGHT
        self.color = "white"

    def draw(self, screen):
        # pygame.draw.rect(screen, "white", pygame.Rect(self.position, (self.width, self.height)), width=5)
        pygame.draw.rect(screen, self.color, self.surface.get_rect(topleft=(self.position[0], self.position[1])), width=2)
        screen.blit(self.surface, self.position)

    def turn(self, angle):
        self.angle += angle
        self.surface = pygame.transform.rotate(self.img, self.angle)
        self.rectangle = self.surface.get_rect(topleft=self.position)
        self.velocity.rotate_ip(-angle)

    def move(self, keys):
        self.handleTeleportation()
        pygame.mixer.init()
        self.position = self.position + self.velocity
        self.rectangle = self.surface.get_rect(topleft=self.position)

        #  sound = pygame.mixer.music.load('assets/rocketengine.wav')
        #  pygame.mixer.music.play()
        #  pygame.mixer.music.stop()

        if keys[self.keyLeft]:
            self.turn(0.5)
        if keys[self.keyRight]:
            self.turn(-0.5)

        if keys[self.keyUp]:
            self.velocity *= 1.01

        if keys[self.keyDown]:
            self.velocity /= 1.01


class Bullet:
    def __init__(self, position, velocity, angle=0):
        self.angle = angle
        self.position = Vector2(position)
        self.velocity = Vector2(velocity).rotate(-self.angle)
        self.settings = readSettings()
        self.width = 4
        self.height = 4
        self.rectangle = pygame.Rect(position, (self.width, self.height))
        self.color = "green"

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle)

    def move(self):
        self.position += self.velocity
        self.rectangle.topleft = self.position

    def collision(self, other):
        return self.rectangle.colliderect(other.rectangle)

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

