name = input("Ведите: ")


def num_translate(name):
    trns = {"one":"один","two":"два","three":"три","four":"четыре","five":"пять","six":"шесть","seven":"семь","eight":"восемь","nine":"девять","десять": "ten"}
    if not bool(name in trns):
        return None
    else:
        return print('"'+str(trns[name])+'"')


num_translate(name)