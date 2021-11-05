from random import randrange
noun = ["автомобиль", "лес", "огонь", "город", "дом"]
adverb = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjective = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
n = int(input("Введите количество шуток: "))
m = input("Повторяются ли слова в шутках: [yes/no] ")


def rand_elem(spis):
    n = spis[randrange(len(spis))]
    return n

def get_jokes(n, m, noun, adverb, adjective):
    i = 0
    jokes = []
    nou = []
    adv = []
    adj = []
    for i in range(n):
        if m == "yes":
            nouns = noun[randrange(len(noun))]
            random_idx2 = randrange(len(adverb))
            adverbs = adverb[random_idx2]
            random_idx3 = randrange(len(adjective))
            adjectives = adjective[random_idx3]
            st = str(nouns) + ' ' + str(adverbs) + ' ' + str(adjectives)
            jokes.append(st)
        elif m == "no":
            nouns = noun[randrange(len(noun))]
            adverbs = adverb[randrange(len(adverb))]
            adjectives = adjective[randrange(len(adjective))]
            nou.append(nouns)
            adv.append(adverbs)
            adj.append(adjectives)
            if nou.count(nouns) > 1:
                while True:
                    g = rand_elem(noun)
                    if g != nouns and not bool(g in nou):
                        nouns = g
                        nou.append(g)
                        break
                    continue
            if adv.count(adverbs) > 1:
                while True:
                    g = rand_elem(adverb)
                    if adverbs != g and not bool(g in adv):
                        adverbs = g
                        adv.append(g)
                        break
                    continue
            if adj.count(adjectives) > 1:
                while True:
                    g = rand_elem(adjective)
                    if adjectives != g and not bool(g in adj):
                        adjectives = g
                        adv.append(g)
                        break
                    continue
            st = str(nouns) + ' ' + str(adverbs) + ' ' + str(adjectives)
            jokes.append(st)
    return jokes

print(get_jokes(n, m, noun, adverb, adjective))