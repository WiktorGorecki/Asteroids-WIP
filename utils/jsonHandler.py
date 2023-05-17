from json import load, dump


def readJSON(filePath):
    with open(filePath, "r") as file:
        data = load(file)
        file.close()
        return data


def writeJSON(filePath, toWrite):
    with open(filePath, "w") as file:
        dump(toWrite, file)