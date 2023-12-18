import json


def sortdict(nameFileWithWords):
    with open(nameFileWithWords, "r", encoding="utf-8") as jsonFile:
        phrases = json.load(jsonFile)
        newPhrased = {}
        for i in sorted(phrases):
            newPhrased[i] = phrases[i]
        with open(nameFileWithWords, "w", encoding="utf-8") as jsonFile2:
            json.dump(newPhrased, jsonFile2)
