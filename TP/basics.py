import random

# I
# 1. Affichage

une_variable = 10
print(1)
print("salut!")
print(1, end="")
print(une_variable)

# 2.Boucles

i = 0
while i <= 100:
    print(i)
    i += 1

for j in range(101):
    print(j)

width = 20
height = 20
creux = False

for w in range(width):
    for h in range(height):
        pass

# 3.Listes
liste_vide = []
liste_pleine = [1, 2, 3, 4]
print(len(liste_pleine))
liste_pleine[2] = 10
liste_pleine.remove(1)
print(liste_pleine)

for el in liste_pleine:
    print(liste_pleine)

i = 0
while i < len(liste_pleine):
    print(liste_pleine[i])
    i += 1

# 4.Aleatoire en Python
print(random.randint(1, 10))
print(random.randrange(1, 100))
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(ma_liste))
random.shuffle(ma_liste)
print(ma_liste)
