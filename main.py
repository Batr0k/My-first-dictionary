import json

import changeDictionary
import mainLearningEnglish
import test


# def reset(nameFileWithWords):
#     with open(nameFileWithWords, "w", encoding="utf-8") as jsonFile:
#         with open(r"C:\Users\Дмитрий\Desktop\Выражения.txt", "r", encoding="utf-8") as file:
#             phrases = file.readlines()
#             phrases.sort(key=lambda x: x.lower())
#             jsonPhrases = {}
#             for i in phrases:
#                 key = i[:i.find('-') - 1].lower()
#                 value = i[i.find('-') + 2:-1].split('; ')
#                 jsonPhrases[key] = value
#             json.dump(jsonPhrases, jsonFile)


def backupDictionary(nameFileWithWords):
    fileForBackup = r"jsonfiles\backupDictionary.json"
    with open(nameFileWithWords, "r", encoding="utf-8") as jsonFile:
        phrases = json.load(jsonFile)
        with open(fileForBackup, "w", encoding="utf-8") as jsonFile2:
            json.dump(phrases, jsonFile2)


def main():
    print("Добро пожаловать! Выйти - \"q\"")
    while True:
        key = input("1)Слова\n2)Выражения\n")
        if key in "qй":
            print("Конец.")
            break
        if key == "1":
            nameFileWithWords = r"jsonfiles\mydictionarywords.json"
        elif key == "2":
            nameFileWithWords = r"jsonfiles\mydictionaryphrases.json"
        else:
            continue
        while True:
            key = input("1)Сделать backup\n2)Пройти тест\n3)Изменить словарь\n4)Учить\n")
            if key in "qй":
                break
            elif key == "1":
                backupDictionary(nameFileWithWords)
            elif key == "2":
                test.test(nameFileWithWords)
            elif key == "3":
                changeDictionary.changeDictionary(nameFileWithWords)
            elif key == "4":
                mainLearningEnglish.printAllWords(nameFileWithWords)



if __name__ == "__main__":
    main()
