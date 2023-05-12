# 1
liste = [17, 38, 10, 25, 72]

liste.sort()
print(liste)

liste.append(12)
print(liste)

liste.reverse()
print(liste)

print(liste.index(17))

liste.remove(38)
print(liste)

print(liste[2:3])

print(liste[:2])

print(liste[-1])

print(liste[3:])

print(liste[::])

print(liste[-1])

# 2
truc = []
machin = [0.0] * 5
print(truc)
print(machin)

print(range(0, 4))
print(range(4, 8))
print(range(2, 9, 2))

chose = [i for i in range(0, 6)]
print(chose)
print(3 in chose)
print(6 in chose)

# 3
added = [i + 3 for i in chose]
print(added)

# 4
added_2 = [i + 3 if i >= 2 else i for i in chose]
print(added_2)

# 5
str_added = [f"{i}{j}" for i in "abc" for j in "de"]
print(str_added)

# 6
somme = sum([i for i in range(10)])
print(somme)

# 7
x = {"a", "b", "c", "d"}
y = {"s", "b", "d"}

print(x)
print(y)

print('c' in x)
print('a' in y)

# ensemble
print(x.difference(y))
print(y.difference(x))
# union
print(x.union(y))

# intersection
print(x.intersection(y))


# 8
def compter_mots(chaine):
    lettres = set(chaine)
    result = {}
    for lettre in lettres:
        result[lettre] = chaine.count(lettre)
    return result


print(compter_mots("barbapapa"))

# 9
dico_ato = {
    "Au": {
        "Te/Tf": [2970, 1063],
        "Z/A": [79, 69.967]
    },
    "Ga": {
        "Te/Tf": [2237, 29.8],
        "Z/A": [31, 69.72]
    }
}

print(dico_ato["Au"]["Z/A"][0])
