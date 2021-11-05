#не получилось сделать
def thesaurus(words):

    names = dict()
    lenw = int(len(words))
    i = 0
    for i in range(lenw):
        if words[i][0] in names:
            names[words[i][0]].append(words[i])
        else:
            g = [words[i]]
            names[words[i][0]] = g
    return names


line = input()
words = line.split(' ')
print(thesaurus(words))
