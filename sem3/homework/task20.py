import re

english_scores = {1:'AEIOULNSTR',
                  2:'DG',
                  3:'BCMP',
                  4:'FHVWY',
                  5:'K',
                  8:'JX',
                  10:'QZ'}
russian_scores = {1:'АВЕИНОРСТ',
                  2:'ДКЛМПУ',
                  3:'БГЁЬЯ',
                  4:'ЙЫ',
                  5:'ЖЗХЦЧ',
                  8:'ШЭЮ',
                  10:'ФЩЪ'}

text = input("Enter your word: ").upper()

def isCyrillic(word):
    return bool(re.search('[а-яА-Я]', word))

sum_ru = 0
sum_en = 0

if isCyrillic(text):
    print(sum([key for symbol in text for key, res in russian_scores.items() if symbol in res]))
    # for symbol in text:
    #     for key, res in russian_scores.items():
    #         if symbol in res:
    #             sum_ru += key
    # print(sum_ru)
else:
    print(sum([key for symbol in text for key, res in english_scores.items() if symbol in res]))
    # for symbol in text:
    #     for key, res in english_scores.items():
    #         if symbol in res:
    #             sum_en += key
    # print(sum_en)