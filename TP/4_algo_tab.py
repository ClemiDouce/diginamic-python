# 1.1
def index_minimum(t, d, f):
    extrait = t[d:f]
    minimum = min(extrait)
    return t.index(minimum)


# 1.2 Tri a bulle
def bubble_parse(t):
    n = len(t)
    for i in range(n):
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]


new_tab = [10, 90, 20, 34, 87, 17, 29, 40]

bubble_parse(new_tab)


# 2.1
def recherche_tant_que():
    pass


def recherche_dycho(tab, a):
    pass