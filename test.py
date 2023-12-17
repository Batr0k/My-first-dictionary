import json
import random


def test(nameFileWithWords):
    with open(nameFileWithWords, "r", encoding="utf-8") as jsonFile:
        phrases = json.load(jsonFile)
        while True:
            print("--------------------------------------------")
            key = random.choice(list(phrases.keys()))
            possible_translation = input(key + "\nВведите один из возможных переводов\n")
            if possible_translation in "qй":
                break
            elif possible_translation in phrases[key]:
                print("Молодец")
            else:
                print("К сожаление, неверно, правильный(ые) перевод(ы):")
                print(*phrases[key], sep=", ")
