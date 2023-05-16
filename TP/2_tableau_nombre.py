# II Tableau de nombres
# a.Tableau d'entier
import random
import time

my_tab = [1, 2, 3, 4, 5, 10, 2, 3, 4, 20, 13, 20]


# 1.Moyenne
def average(tab):
    return sum(tab) / len(tab)


# 2.Nombre d'occurence
def occurence_count(tab, searched):
    return my_tab.count(searched)


# 3.Nombre d'element superieurs ou egaux a 10
def superior_than_10(tab):
    return len([x for x in tab if x >= 10])


# 4.Valeur maximal
def maximum_value(tab):
    return max(tab)


# 5.Element present
def element_is_in(tab, element):
    return element in tab


# b.fonction pour taille n
# 1.Tableau aleatoire
def random_int_tab(n: int):
    return [random.randint(1, 100) for _ in range(n)]


# 2.tableau premiers entier mélangé
def first_int_shuffled(n: int):
    tab = random_int_tab(n)
    random.shuffle(tab)
    return tab


# 3.Calcul du temps
# Moyenne
random_tab = first_int_shuffled(999999)
print(len(random_tab))
moyenne_time = time.time()
average(random_tab)
print(f"Temps pour la fonction moyenne: {time.time() - moyenne_time}")

# Chercher élement
recherche_time = time.time()
element_is_in(random_tab, 5)
print(f"Temps pour la fonction recherche d'element: {time.time() - recherche_time}")

