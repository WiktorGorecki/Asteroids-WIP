import pygame
from objects.object import GameObject
from objects.spaceship import Spaceship
from objects.asteroid import Asteroid

class Game:
    def __init__(self):
        shipImg = pygame.image.load("assets/ship.svg")
        shipImg2 = pygame.image.load("assets/ship.svg")
        asteroidImg = pygame.image.load("assets/asteroid2.svg")
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.spaceship = Spaceship((400, 300), (0.2,0.2), shipImg)
        self.keyPressed = []
        self.asteroids = [Asteroid((400, 300), (0.3,0.3), asteroidImg)]
        # self.asteroids = [Asteroid((0, 0)) for _ in range(6)]

    # def _get_game_objects(self):
    #     return [*self.asteroids, self.spaceship]

    def main_loop(self):
        while True:
            keys = pygame.key.get_pressed()
            self._handle_input(keys)
            self._process_game_logic()
            self._draw()



    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("ASTEROIDS")

    def _handle_input(self, keys):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

        self.keyPressed = keys

    def _process_game_logic(self):
        self.spaceship.move(self.keyPressed)
        for asteroid in self.asteroids:
            asteroid.move()

        # for game_object in self._get_game_objects():
        #     game_object.move(self.screen)

    def _draw(self):
        self.screen.fill("black")
        self.spaceship.draw(self.screen)

        for asteroid in self.asteroids:
            asteroid.draw(self.screen)

        pygame.display.flip()



# def _process_game_logic(self):
#     for game_object in self._get_game_objects():
#         game_object.move(self.screen)
#
#     if self.spaceship:
#         for asteroid in self.asteroids:
#             if asteroid.collides_with(self.spaceship):
#                 self.spaceship = None
#                 break
#
#     for bullet in self.bullets[:]:
#         for asteroid in self.asteroids[:]:
#             if asteroid.collides_with(bullet):
#                 self.asteroids.remove(asteroid)
#                 self.bullets.remove(bullet)
#                 asteroid.split()
#                 break
#
#     for bullet in self.bullets[:]:
#         if not self.screen.get_rect().collidepoint(bullet.position):
#             self.bullets.remove(bullet)