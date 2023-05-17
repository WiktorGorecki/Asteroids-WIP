import pygame

from objects.object import GameObject

class Spaceship(GameObject):
    def __init__(self, position, velocity):
        print("Debug: Creating new Spaceship object")
        GameObject.__init__(self, position, velocity)
        self.keyUp = pygame.K_UP
        self.keyDown = pygame.K_DOWN
        self.keyLeft = pygame.K_LEFT
        self.keyRight = pygame.K_RIGHT

    def draw(self, surface):
        # blit_position = self.position - Vector2(self.radius)
        # surface.blit(self.sprite, blit_position)
        pygame.draw.rect(surface, "green", pygame.Rect(self.position[0], self.position[1], self.height, self.width))
        #pygame.draw.rect(surface, "green", self.position)


    def move(self, keys):
        if keys[self.keyUp]:
            self.position[1] -= self.velocity[1]
        elif keys[self.keyDown]:
            self.position[1] += self.velocity[1]
        elif keys[self.keyLeft]:
            self.position[0] -= self.velocity[0]
        elif keys[self.keyRight]:
            self.position[0] += self.velocity[0]