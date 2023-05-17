import pygame
from objects.object import GameObject

class Game:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        # self.spaceship = Spaceship((400, 300))
        self.object = GameObject(
            (400, 300), (0, 0)
        )

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("ASTEROIDS")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

    def _process_game_logic(self):
        pass
        #self.spaceship.move()

    def _draw(self):
        # self.screen.blit(self.background, (0, 0))
        self.screen.fill("black")
        self.object.draw(self.screen)
        pygame.display.flip()