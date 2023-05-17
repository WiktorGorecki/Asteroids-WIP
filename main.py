import pygame
from pygame import QUIT, KEYDOWN, MOUSEBUTTONDOWN, FULLSCREEN, DOUBLEBUF, SCALED

from game import Game
from utils.settings import readSettings

pygame.init()

pygame.event.set_allowed([QUIT, KEYDOWN, MOUSEBUTTONDOWN])  # If you need event to be handled - add it to the list.
# Only add these events, which are needed to save performance

settings = readSettings()

if settings["fullscreen"]:
    flags = FULLSCREEN | DOUBLEBUF
else:
    flags = SCALED | DOUBLEBUF

# Screen initialisation
SCREEN = pygame.display.set_mode((settings["width"], settings["height"]), flags, 1)
SCREEN.set_alpha(None)
pygame.display.set_caption("Pong")

game = Game()
game.main_loop()