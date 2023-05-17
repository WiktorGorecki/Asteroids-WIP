from utils.jsonHandler import readJSON, writeJSON


def writeRankingSingle(toWrite):
    writeJSON("./rankingSingle.json", toWrite)

def readRankingSingle():
    return readJSON("./rankingSingle.json")

def rankingSingleLenghtCheck():
    ranking = readRankingSingle()
    if len(ranking) < 10:
        for i in range(len(ranking)+1,11,1):
            nullscore = {"initials": "NUL", "score": 000}
            ranking[str(i)] = nullscore
        writeRankingSingle(ranking)

def addHighScoreSingle(initials, score):
    rankingSingleLenghtCheck()
    ranking = readRankingSingle()
    for i in ranking:
        if score > ranking[i]["score"]:
            tmpinitials = ranking[i]["initials"]
            tmpscore = ranking[i]["score"]
            ranking[i]["initials"] = initials
            ranking[i]["score"] = score
            initials = tmpinitials
            score = tmpscore
    writeRankingSingle(ranking)
