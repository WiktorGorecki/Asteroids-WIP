from utils.jsonHandler import readJSON, writeJSON



def writeRanking(toWrite):
    writeJSON("./ranking.json", toWrite)

def readRanking():
    return readJSON("./ranking.json")

def rankingLenghtCheck():
    ranking = readRanking()
    if len(ranking) < 10:
        for i in range(len(ranking)+1,11,1):
            nullscore = {"initials": "NUL", "score": 000}
            ranking[str(i)] = nullscore
        writeRanking(ranking)

def addHighScore(initials, score):
    rankingLenghtCheck()
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
