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
    print("Debug: Adding highscore for singleplayer")
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

######################################################

def writeRankingDouble(toWrite):
    writeJSON("./rankingDouble.json", toWrite)

def readRankingDouble():
    return readJSON("./rankingDouble.json")

def rankingDoubleLenghtCheck():
    ranking = readRankingDouble()
    if len(ranking) < 10:
        for i in range(len(ranking)+1,11,1):
            nullscore = {"initials1": "NUL", "initials2": "NUL", "score": 000}
            ranking[str(i)] = nullscore
        writeRankingDouble(ranking)

def addHighScoreDouble(initials1, initials2, score):
    print("Debug: Adding highscore for doubleplayer")
    rankingDoubleLenghtCheck()
    ranking = readRankingDouble()
    for i in ranking:
        if score > ranking[i]["score"]:
            tmpinitials1 = ranking[i]["initials1"]
            tmpinitials2 = ranking[i]["initials2"]
            tmpscore = ranking[i]["score"]
            ranking[i]["initials1"] = initials1
            ranking[i]["initials2"] = initials2
            ranking[i]["score"] = score
            initials1 = tmpinitials1
            initials2 = tmpinitials2
            score = tmpscore
    writeRankingDouble(ranking)