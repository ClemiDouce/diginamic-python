my_tab = [1, 2, 3, 4, 5, 10, 2, 3, 4, 20, 13, 20]


# Moyenne
def average(tab):
    return sum(my_tab) / len(my_tab)


# Nombre d'occurence
def occurence_count(tab, searched):
    return my_tab.count(searched)


# Nombre d'element superieurs ou egaux a 10
def superior_than_10(tab):
    return len([x for x in my_tab if x >= 10])


# Element present
def element_is_in(tab, element):
    return element in my_tab
