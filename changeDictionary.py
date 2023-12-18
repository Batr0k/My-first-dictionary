import json

import sortDictionary


def addToDictionary( phrases, nameFileWithWords):
    engWord = input("Введите английское слово:\n").lower().strip()
    if engWord in phrases:
        print("Ошибка, такое слово уже есть в словаре")
        return
    ruWords = input("Введите через \";\" переводы для этого слова\n").split(";")
    phrases[engWord] = list(map(str.lower, ruWords))
    with open(nameFileWithWords, "w", encoding="utf-8") as jsonFile:
        json.dump(phrases, jsonFile)


def addTranslateToDictionary(phrases, nameFileWithWords):
    engWord = input("Введите английское слово:\n").lower()
    if engWord in phrases:
        ruWords = input("Введите новые слова через \";\" для добавления\n").split('; ')
        phrases[engWord] += list(map(str.lower, ruWords))
        with open(nameFileWithWords, "w", encoding="utf-8") as jsonFile:
            json.dump(phrases, jsonFile)
    else:
        print("Такого слова нет")


def changeTranslationWord( phrases, nameFileWithWords):
    engWord = input("Введите английское слово:\n").lower()
    if engWord in phrases:
        ruWords = input("Введите новые слова через \";\" для обновления\n").split('; ')
        phrases[engWord] = list(map(str.lower, ruWords))
        with open(nameFileWithWords, "w", encoding="utf-8") as jsonFile:
            json.dump(phrases, jsonFile)
    else:
        print("Такого слова нет")


def moveToLearned( phrases, nameFileWithWords):  # нужно сделать без загрузки всего файла в память!!!
    nameFileWithLearnedPhrases = r"jsonfiles\learnedPhrases.json"
    engWord = input("Введите английское слово\n").lower()
    if engWord not in phrases:
        print("Такого слова нет в словаре")
        return
    with open(nameFileWithLearnedPhrases, "r+", encoding="utf-8") as jsonFile:
        learnedPhrases = json.load(jsonFile)
    learnedPhrases[engWord] = phrases[engWord]
    with open(nameFileWithLearnedPhrases, "w", encoding="utf-8") as jsonFile:
        json.dump(learnedPhrases, jsonFile)
    del phrases[engWord]
    with open(nameFileWithWords, "w", encoding="utf-8") as jsonFile:
        json.dump(phrases, jsonFile)

def deleteWord(nameFileWithWords):
    with open(nameFileWithWords, "r", encoding="utf-8") as jsonFile:
        phrases = json.load(jsonFile)
    engWord = input("Введите английское слово\n").lower()
    if engWord not in phrases:
        print("Такого слова нет в словаре")
        return
    del phrases[engWord]
    with open(nameFileWithWords, "w", encoding="utf-8") as jsonFile:
        json.dump(phrases, jsonFile)
def changeDictionary(nameFileWithWords):
    with open(nameFileWithWords, "r", encoding="utf-8") as jsonFile:
        phrases = json.load(jsonFile)
    while True:
        print(
            "1) Добавить новое слово и перевод к нему\n2) Добавить перевод к слову\n3) Изменить перевод у слова\n4) Переместить слово в \"Выученное\"\n5) Удалить слово\n")
        key = input().lower()
        if key in "qй":
            break
        if key == "1":
            addToDictionary(phrases, nameFileWithWords)
        elif key == "2":
            addTranslateToDictionary(phrases, nameFileWithWords)
        elif key == "3":
            changeTranslationWord(phrases, nameFileWithWords)
        elif key == "4":
            moveToLearned(phrases, nameFileWithWords)
        elif key == "5":
            deleteWord(nameFileWithWords)
        else:
            print("Неверная цифра")
    sortDictionary.sortdict(nameFileWithWords)
