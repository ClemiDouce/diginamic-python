from random_word import RandomWords

r = RandomWords()

# Choisir un mot au hasard
mot_a_trouver = r.get_random_word()
try_count = 0
letter_used = set()

mot_cache = ["_" for char in mot_a_trouver]
print(mot_a_trouver)
print(mot_cache)

# Boucle de jeu
while "_" in mot_cache:
    print(f"Lettres déja utilisé : {letter_used}")
    player_input = input("Entrez une lettre ou '?' pour abandonner : ")
    if player_input == "?":
        print("Au revoir !")
        break
    if len(player_input) > 1:
        print("Il faut entrer une lettre")
        continue

    if player_input in letter_used:
        print(f"Vous avez déja utilisé la lettre {player_input}")
        continue

    if player_input in mot_a_trouver:
        for index, i in enumerate(mot_a_trouver):
            if i == player_input:
                mot_cache[index] = player_input
        print(mot_cache)
    else:
        print("Cette lettre n'est pas dans le mot a trouver")

    letter_used.add(player_input)
    try_count += 1
else:
    print(f"Bravo, vous avez trouvé en {try_count} essais")
