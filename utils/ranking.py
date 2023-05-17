import pygame

from utils.jsonHandler import readJSON, writeJSON


def readRanking():
    return readJSON("./ranking.json")


def writeRanking(toWrite):
    writeJSON("./ranking.json", toWrite)

def addHighScore(initials, score):
    
