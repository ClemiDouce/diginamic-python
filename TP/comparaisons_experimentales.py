# V
# 1.
import copy
import random
import time
from algo_tab import tri_bulles, tri_insertion, tri_extraction


def copie(t):
    return copy.copy(t)


def inverse(t):
    return copie(t)[::-1]


def tableau_premiers_entiers(n: int):
    return [x for x in range(1, n)]


def tableau_premiers_entiers_melanges(n: int):
    tab = tableau_premiers_entiers(n)
    random.shuffle(tab)
    return tab


def tableau_premiers_entier_inverses(n: int):
    return inverse(tableau_premiers_entiers(n))


def ligne_dans_fichier(f, n, t):
    with open(f, "a") as file:
        file.write(f"{str(n)}\t{str(t)}\n")


def calcul_temps_fonction(t, f):
    tab = copie(t)
    begin = time.time()
    f(tab)
    return time.time() - begin


def stats_melangees(nmin, nmax, pas, fois, fonction, nom_fichier):
    results = [
        f"Resultats pour tableaux mélangées de taille {nmin} a {nmax} avec un pas de {pas}, genere {fois} fois:\n"
    ]
    for taille in range(nmin, nmax, pas):
        tab_time = []
        for i in range(fois):
            tab = tableau_premiers_entiers_melanges(taille)
            tab_time.append(calcul_temps_fonction(tab, fonction))
        moyenne_time = sum(tab_time) / len(tab_time)
        results.append(f"Temps moyen pour taille {taille}: {moyenne_time}\n")
        ligne_dans_fichier(f"datas/stats_tab_melanges_{nom_fichier}.dat", taille, moyenne_time)


def stats_ordonnees(nmin, nmax, pas, fois, fonction, nom_fichier):
    results = [
        f"Resultats pour tableaux ordonnees de taille {nmin} a {nmax} avec un pas de {pas}, genere {fois} fois:\n"
    ]
    for taille in range(nmin, nmax, pas):
        tab_time = []
        for i in range(fois):
            tab = tableau_premiers_entiers(taille)
            tab_time.append(calcul_temps_fonction(tab, fonction))
        moyenne_time = sum(tab_time) / len(tab_time)
        results.append(f"Temps moyen pour taille {taille}: {sum(tab_time) / len(tab_time)}\n")
        ligne_dans_fichier(f"datas/stats_tab_ordonnees_{nom_fichier}.dat", taille, moyenne_time)


def stats_inversees(nmin, nmax, pas, fois, fonction, nom_fichier):
    results = [
        f"Resultats pour tableaux inversé de taille {nmin} a {nmax} avec un pas de {pas}, genere {fois} fois:\n"
    ]
    for taille in range(nmin, nmax, pas):
        tab_time = []
        for i in range(fois):
            tab = tableau_premiers_entier_inverses(taille)
            tab_time.append(calcul_temps_fonction(tab, fonction))
        moyenne_time = sum(tab_time) / len(tab_time)
        results.append(f"Temps moyen pour taille {taille}: {sum(tab_time) / len(tab_time)}\n")
        ligne_dans_fichier(f"datas/stats_tab_inversees_{nom_fichier}.dat", taille, moyenne_time)


# first_tab = [1, 2, 3, 4]
# new_tab = copie(first_tab)
# first_tab.append(10)
# print(new_tab, first_tab)
# print(inverse(new_tab))

print("go")
# Tri melange
stats_melangees(100, 2000, 100, 5, tri_extraction, "extraction")
stats_melangees(100, 2000, 100, 5, tri_insertion, "insertion")
stats_melangees(100, 2000, 100, 5, tri_bulles, "bulle")
print("Fin des stats mélangées")

# Tri ordonnees
stats_ordonnees(100, 2000, 100, 5, tri_extraction, "extraction")
stats_ordonnees(100, 2000, 100, 5, tri_insertion, "insertion")
stats_ordonnees(100, 2000, 100, 5, tri_bulles, "bulle")
print("Fin des stats ordonnées")

# Tri inversées
stats_inversees(100, 2000, 100, 5, tri_extraction, "extraction")
stats_inversees(100, 2000, 100, 5, tri_insertion, "insertion")
stats_inversees(100, 2000, 100, 5, tri_bulles, "bulle")
print("Fin des stats inversees")
