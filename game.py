from random import random, randint
from random import randrange

import pygame

from objects.object import GameObject
from objects.spaceship import Spaceship
from objects.asteroid import Asteroid

from utils.get_font import get_font

from screens.main_menu import main_menu
from screens.rankingAddSingle import rankingAddSingle
from utils import settings

from utils.settings import readSettings
from objects.spaceship import Bullet
from pygame.math import Vector2
from utils.scoreHandler import scoreHandler
from utils.stats import stats
from utils.discord import getApp

class Game:
    def __init__(self):
        print("Debug: Resetting stats")
        stats['score'] = 0
        stats['healthPoints'] = 3
        shipImg = pygame.image.load("assets/ship.svg")
        asteroidImg = pygame.image.load("assets/asteroid2.svg")
        self.settings = readSettings()
        self.screen = pygame.display.set_mode((1280, 720))
        self.spaceship = Spaceship((400, 300), (2,2), shipImg)
        self.keyPressed = []
        self.asteroids = [Asteroid((0.8, 0.8), asteroidImg) for i in range(10)]
        self.bullets = []
        self.clock = pygame.time.Clock()
        self.bulletInterval = 300
        self.lastBulletTime = pygame.time.get_ticks()

    # def _get_game_objects(self):
    #     return [*self.asteroids, self.spaceship]

    def main_loop(self, SCREEN):
        while 1:
            keys = pygame.key.get_pressed()
            self._handle_input(keys)
            self._process_game_logic()
            self._draw()
            if stats["healthPoints"] == 0:
                rankingAddSingle(SCREEN, stats["score"])

            self.clock.tick(60)
            if readSettings()["discord"]:
                getApp().run_callbacks()

    def _handle_input(self, keys):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

        self.keyPressed = keys
        if (keys[pygame.K_SPACE]):
            if pygame.time.get_ticks() - self.lastBulletTime > self.bulletInterval:
                self.lastBulletTime = pygame.time.get_ticks()
                ox, oy = self.spaceship.position[0]+self.spaceship.width//2, self.spaceship.position[1]
                # px, py = self.spaceship.position[0] + self.spaceship.width//2, self.spaceship.position[1] + self.spaceship.height//2
                px, py = self.spaceship.rectangle.center
                # qx = ox + math.cos(self.spaceship.angle) * (px - ox) - math.sin(self.spaceship.angle) * (py - oy)
                # qy = oy + math.sin(self.spaceship.angle) * (px - ox) + math.cos(self.spaceship.angle) * (py - oy)

                bulletPosition = (px, py)
                pygame.draw.rect(self.screen, "blue", pygame.Rect(bulletPosition, (5, 5)))

                self.bullets.append(Bullet(bulletPosition, (self.spaceship.velocity*5).rotate(self.spaceship.angle), self.spaceship.angle))
                shootingSound = pygame.mixer.Sound('./assets/lazershoot.wav')
                pygame.mixer.Sound.play(shootingSound)
                pygame.mixer.music.stop()

    def _process_game_logic(self):
        self.spaceship.move(self.keyPressed)
        for asteroid in self.asteroids:
            asteroid.move()

        for bullet in self.bullets:
            bullet.move()
            if bullet.handleCollisionDown() or bullet.handleCollisionTop() or bullet.handleCollisionLeft() or bullet.handleCollisionRight():
                self.bullets.remove(bullet)


        for asteroid in self.asteroids:
            if self.spaceship.collision(asteroid):
                # print("collision")
                collisionSound = pygame.mixer.Sound('./assets/meteorecrush.wav')
                pygame.mixer.Sound.play(collisionSound)
                pygame.mixer.music.stop()

                self.spaceship.color = "red"
                self.asteroids.remove(asteroid)
                scoreHandler("onShipHit")
            else:
                self.spaceship.color = "white"

        for asteroid in self.asteroids:
            for asteroid2 in self.asteroids:
                if asteroid.collision(asteroid2):
                    if asteroid != asteroid2:
                        # magic
                        bl = asteroid2.rectangle.left - asteroid.rectangle.width / 4
                        br = asteroid2.rectangle.right + asteroid.rectangle.width / 4
                        nv = (0, 1) if bl < asteroid.rectangle.centerx < br else (1, 0)
                        asteroid.velocity.reflect_ip(nv)

                        # print(asteroid.velocity)
                        # asteroid.velocity.reflect_ip(Vector2(0, -1))
                        # print(asteroid.velocity)
                        # asteroid2.velocity.reflect_ip(Vector2(-1, -1))
                        # asteroid.velocity.reflect_ip(-asteroid.velocity.normalize())
                        # asteroid2.velocity.reflect_ip(-asteroid2.velocity.normalize())
                        # asteroid.velocity *= -1
                        # asteroid2.velocity *= -1
            for bullet in self.bullets:
                if bullet.collision(asteroid):
                # print("collision")
                    bullet.color = "red"
                    asteroid.health -= 1
                    scoreHandler("onAsteroidHit")
                    bulletHittingSound = pygame.mixer.Sound('./assets/meteorpoint.wav')
                    pygame.mixer.Sound.play(bulletHittingSound)
                    pygame.mixer.music.stop()

                    if asteroid.checkDestroy():
                        self.asteroids.remove(asteroid)
                else:
                    bullet.color = "green"

    def _draw(self):
        self.screen.fill("black")
        SCORE_TEXT = get_font(25).render("SCORE:", True, "green")
        SCORE_RECT = SCORE_TEXT.get_rect(center=(50, 50))
        self.screen.blit(SCORE_TEXT, SCORE_RECT)

        NUMBER_TEXT = get_font(25).render(str(stats['score']), True, "green")
        NUMBER_RECT = NUMBER_TEXT.get_rect(center=(150, 50))
        self.screen.blit(NUMBER_TEXT, NUMBER_RECT)

        heart = pygame.image.load('assets/heart.svg')
        for i in range(0, stats['healthPoints']):
            HEART_ICON = pygame.transform.scale(heart, (25, 25))
            HEART_RECT = HEART_ICON.get_rect(center=(50 + i * 25, 100))
            self.screen.blit(HEART_ICON, HEART_RECT)

        if stats['healthPoints'] <= 0:
            from screens.rankingAddSingle import rankingAddSingle
            rankingAddSingle(self.screen, stats['score'])

        self.spaceship.draw(self.screen)
        for asteroid in self.asteroids:
            asteroid.draw(self.screen)

        for bullet in self.bullets:
            bullet.draw(self.screen)

        pygame.display.flip()
