def pile(*elements):
    return [i for i in elements]


def empile(add_pile, element):
    add_pile.append(element)
    return add_pile


def depile(remove_pile):
    remove_pile.pop(len(remove_pile) - 1)


ma_pile = pile("salut", "mes", "ptites", "beaute")
empile(ma_pile, "erreur")
print(ma_pile)
depile(ma_pile)
print(ma_pile)
