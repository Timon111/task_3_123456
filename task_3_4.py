

def thesaurus(words):
    names = dict()
    surnames = dict()
    i = 0
    for i in range(int(len(words))):
        if words[i][0] in names:
            names[words[i][0]].append(words[i])
            surnames[words[i][0]].append(names[words[i][0]])
        else:
            g = [words[i]]
            names[words[i][0]] = g
            surnames[words[i][0]] = names[words[i][0]]
    return print(surnames)


line = input()
words = line.split(' ')
i = 0
for i in range(int(len(words) / 2)):
    words[i] += ' ' + words[int(i+1)]
    i += 1
del words[int(len(words) / 2):int(len(words))]
thesaurus(words)
