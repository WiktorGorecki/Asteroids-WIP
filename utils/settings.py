import pygame

from utils.jsonHandler import readJSON, writeJSON


def readSettings():
    return readJSON("./settings.json")


def writeSettings(toWrite):
    writeJSON("./settings.json", toWrite)

def refreshWindow(SCREEN):
    settings = readSettings()
    resized_screen = pygame.transform.scale(SCREEN, (settings["width"], settings["height"]))
    SCREEN.blit(resized_screen, (0, 0))
    return SCREEN