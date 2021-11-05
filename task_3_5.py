from random import randrange
noun = ["автомобиль", "лес", "огонь", "город", "дом"]
adverb = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjective = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n = int(input("Введите количество шуток: "))


def get_jokes(n, noun, adverb, adjective):
    i = 0
    jokes = []
    for i in range(n):
        nouns = noun[randrange(len(noun))]
        random_idx2 = randrange(len(adverb))
        adverbs = adverb[random_idx2]
        random_idx3 = randrange(len(adjective))
        adjectives = adjective[random_idx3]
        jokes.append(str(nouns) + ' ' + str(adverbs) + ' ' + str(adjectives))
    return jokes

print(get_jokes(n, noun, adverb, adjective))