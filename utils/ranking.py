import pygame

from utils.jsonHandler import readJSON, writeJSON


def readRanking():
    return readJSON("./ranking.json")


def writeRanking(toWrite):
    writeJSON("./ranking.json", toWrite)

def addHighScore(initials, score):
    ranking = readRanking()
    for i in ranking:
        if score > ranking[i]["score"]:
            tmpinitials = ranking[i]["initials"]
            tmpscore = ranking[i]["score"]
            ranking[i]["initials"] = initials
            ranking[i]["score"] = score
            initials = tmpinitials
            score = tmpscore
    writeRanking(ranking)
