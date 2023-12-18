import json


def printAllWords(nameFileWithWords):
    with open(nameFileWithWords, "r", encoding="utf-8") as jsonFile:
        phrases = json.load(jsonFile)
        for i in phrases.items():
            print(i[0], "-", end=" ")
            print(*i[1], sep="; ")
