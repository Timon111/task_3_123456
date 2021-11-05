name = input("Ведите цифру: ")


def num_translate(name):
    trns = {"one":"один","two":"два","three":"три","four":"четыре","five":"пять","six":"шесть","seven":"семь","eight":"восемь","nine":"девять","десять": "ten"}
    if name[0].isupper():
        up = True
        name = name.lower()
        return print('"' + trns[name].capitalize() + '"')
    elif not bool(name[0].isupper()):
        return print('"' + trns[name] + '"')
    else:
        return None


num_translate(name)