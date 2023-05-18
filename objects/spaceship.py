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
        pygame.draw.rect(screen, self.color, self.surface.get_rect(topleft=(self.position[0], self.position[1])), width=5)
        pygame.draw.rect(screen, "blue", pygame.Rect(self.position.rotate(self.angle),( 4, 4)))
        screen.blit(self.surface, self.position)

    def turn(self, angle):
        self.angle += angle
        self.surface = pygame.transform.rotate(self.img, self.angle)
        self.rectangle = self.surface.get_rect(topleft=self.position)
        self.velocity.rotate_ip(-angle)

    def move(self, keys):
        self.handleTeleportation()
        pygame.mixer.init()

        #  sound = pygame.mixer.music.load('assets/rocketengine.wav')
        #  pygame.mixer.music.play()
        #  pygame.mixer.music.stop()

        if keys[self.keyLeft]:
            self.turn(0.5)
        if keys[self.keyRight]:
            self.turn(-0.5)

        if keys[self.keyUp]:
            self.position += self.velocity
            self.rectangle = self.surface.get_rect(topleft=self.position)

            # self.velocity += (0.1, 0.1)

            # dx = self.velocity[0]*0.1 * math.cos(math.radians(self.angle + 90))
            # dy = -self.velocity[1]*0.1 * math.sin(math.radians(self.angle + 90))
            # self.rectangle.move_ip(dx, dy)
            # self.position = self.rectangle.center
            # print(self.rectangle.center)

        # if keys[self.keyDown]:
        #     if (self.velocity[0]-0.1>0):
        #         self.velocity-=(0.1,0.1)
        #
        # if keys[self.keyUp]:
        #     self.velocity += (0.1, 0.1)
# class Bullet(GameObject):
#     def __init__(self):
#
#         self.point = player.head
#         self.position =
#         self.y = self.point
#         self.width = 4
#         self.height = 4
#         self.c = player.cosine
#         self.s = player.sine
#         self.xv = self.c * 10
#         self.yv = self.s * 10
#
#     def move(self):
#         self.x += self.xv
#         self.y -= self.yv
#
#     def draw(self, win):
#         pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.w, self.h])
#
#     def checkOffScreen(self):
#         if self.x < -50 or self.x > sw or self.y > sh or self.y < -50:
#             return True


class Bullet:
    def __init__(self, position, velocity, angle=0):
        self.angle = angle
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.settings = readSettings()
        self.width = 5
        self.height = 9
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


# class Bullet(GameObject):
#
#     def __init__(self, position, velocity):
#         print("Debug: Creating new bullet object")
#         GameObject.__init__(self, position, (0.2, 0.2), Surface, angle=randint(0, 360))
#
#
#
#     def turn(self, angle):
#         self.angle += angle
#         self.surface = pygame.transform.rotate(self.img, self.angle)
#         self.rectangle = self.surface.get_rect(topleft=self.position)
#         self.velocity.rotate_ip(-angle)
#
#     def move(self):
#         self.handleTeleportation()
#
#         self.position += self.velocity
#         self.rectangle = self.surface.get_rect(topleft=self.position)
#         # self.turn(0.1)
