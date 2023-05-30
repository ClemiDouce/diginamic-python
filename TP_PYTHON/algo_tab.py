# 1.1
import copy

from tableau_nombre import first_int_shuffled


def index_minimum(tab):
    # extrait = tab[debut:fin]
    minimum = min(tab)
    return tab.index(minimum)


# 1.2 Tri a bulle
def tri_bulles(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]


# 2.1
def recherche_tant_que():
    pass


# 2.2
def recherche_dycho(tab, a):
    begin, end = 0, len(tab)
    while begin <= end:
        new_index = (begin + end) // 2
        element = tab[new_index]
        if element == a:
            return True
        elif element < a:
            begin = new_index + 1
        else:
            end = new_index - 1

    return False


# 3.
def tri_extraction(tab):
    copy_tab = copy.copy(tab)
    result = []
    for i in range(len(tab)):
        index_mini = index_minimum(copy_tab)
        elem = copy_tab[index_mini]
        result.append(elem)
        copy_tab.remove(elem)
    return result


def tri_insertion(tab):
    for i in range(1, len(tab) - 1):
        x = tab[i]
        j = i
        while j > 0 and tab[j - 1] > x:
            tab[j] = tab[j - 1]
            j = j - 1
        tab[j] = x


my_tab = first_int_shuffled(100)
tri_insertion(my_tab)
new_tab = tri_extraction(my_tab)
print(new_tab)
