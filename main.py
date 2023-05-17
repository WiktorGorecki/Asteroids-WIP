# Imports
import pygame
from pygame import QUIT, KEYDOWN, MOUSEBUTTONDOWN, FULLSCREEN, DOUBLEBUF, SCALED

from game import Game
from utils.settings import readSettings
pygame.init()

pygame.event.set_allowed([QUIT, KEYDOWN, MOUSEBUTTONDOWN])  # If you need event to be handled - add it to the list.
# Only add these events, which are needed to save performance

settings = readSettings()

print("\nDebug: Creating game window")
print("     -Resolution:    "+str(settings["width"])+"x"+str(settings["height"]))
# Setting flags for screen option
if settings["fullscreen"]:
    print("     -Display mode:    " + str(" Fullscreen"))
    flags = FULLSCREEN | DOUBLEBUF  # Flags for fullscreen
else:
    print("     -Display mode: " + str(" Scaled"))
    flags = SCALED | DOUBLEBUF  # Flags for window

# Screen initialisation
SCREEN = pygame.display.set_mode((settings["width"], settings["height"]), flags, 1)
SCREEN.set_alpha(None)  # No alpha channel
pygame.display.set_caption("Asteroids")


game = Game()
game.main_loop()