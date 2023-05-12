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


def compter_mots(chaine):
    lettres = set(chaine)
    result = {}
    for lettre in lettres:
        result[lettre] = chaine.count(lettre)
    return result


print(compter_mots("barbapapa"))

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

chaine = "bonjour"
