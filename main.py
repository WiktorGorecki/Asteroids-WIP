# Imports
import pygame
from pygame import QUIT, KEYDOWN, MOUSEBUTTONDOWN, FULLSCREEN, DOUBLEBUF, SCALED

from game import Game
from utils.settings import readSettings
from utils.ranking import addHighScore

pygame.init()

pygame.event.set_allowed([QUIT, KEYDOWN, MOUSEBUTTONDOWN])  # If you need event to be handled - add it to the list.
# Only add these events, which are needed to save performance

settings = readSettings()

# Setting flags for screen option
if settings["fullscreen"]:
    flags = FULLSCREEN | DOUBLEBUF  # Flags for fullscreen
else:
    flags = SCALED | DOUBLEBUF  # Flags for window

print("\nDebug: Creating game window")
print("     -Running in "+str(settings["width"])+"x"+str(settings["height"])+" resolution")
print("     -Display mode "+str(flags))
# Screen initialisation
SCREEN = pygame.display.set_mode((settings["width"], settings["height"]), flags, 1)
SCREEN.set_alpha(None)  # No alpha channel
pygame.display.set_caption("Asteroids")

# addHighScore("BBB", 123)

game = Game()
game.main_loop()