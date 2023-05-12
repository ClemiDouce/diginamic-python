import math


# III.1
# def table(base, debut, fin, inc):
#     print("Debut de fonction")
#     # Check
#
#     # Execution
#     for i in range(debut, fin, inc):
#         print(base * i)
#
#
# table(5, 2, 10, 3)


# III.2

def cube(value):
    return value ** 3


def volume_sphere(rayon):
    v = 4 / 3 * math.pi * cube(rayon)
    return v


volume_sphere(10)


# III.3
# Écrire une fonction maFonction qui retourne f (x) Æ 2x3Åx ¡5.
# Problème de caractères spéciaux
# f(x) = 2x3 + x - 5

def ma_fonction(x):
    f = 2 * 3 + x - 5
    return f


def tabuler(fonction, borneInf, borneSup, nbPas):
    pass


# III.4
def volMasseEllipsoide(a=0, b=0, c=0, masseVolumique=0):
    volume = 4 / 3 * math.pi * a * b * c
    masse = volume * masseVolumique

    return volume, masse


# III.5
def somme(tuple):
    return sum(tuple)


print(somme((1, 2, 3, 4, 5)))
print(somme((1, 2, 3, 4, 5, 23, 2, 1, 34, 54, 2, 43)))
print(somme((1, 2, 3, 4, 5, 10, 14, 123)))


# III.6
def somme_v2(p1, p2, p3):
    return p1 + p2 + p3


mon_tuple = (10, 20, 30)
print(somme_v2(*mon_tuple))


# III.7
def un_dictionnaire(dico):
    print(dico)


def un_dictionnaire_v2(*args, **param):
    print(param)


mon_dico = {"ma_cle": 10, "ma_cles": 20, "ma_cless": 30}
print(type(mon_dico.keys()))
print(mon_dico.values())
un_dictionnaire_v2(1, 2, 3, param=10)
