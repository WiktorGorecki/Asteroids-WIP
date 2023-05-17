import pygame.draw
from pygame.math import Vector2

class GameObject:
    def __init__(self, position, velocity):
        self.angle = 0
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.height = 40
        self.width = 40

    def draw(self, surface):
        # blit_position = self.position - Vector2(self.radius)
        # surface.blit(self.sprite, blit_position)
        pygame.draw.rect(surface, "green", pygame.Rect(0,0, self.height, self.width))

    def move(self):
        self.position = self.position + self.velocity

    # def collides_with(self, other_obj):
    #     distance = self.position.distance_to(other_obj.position)
    #     return distance < self.radius + other_obj.radius