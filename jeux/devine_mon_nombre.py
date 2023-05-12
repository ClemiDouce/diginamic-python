import random

try_number = 1
player_number = -1

random_number = random.randint(1, 31)
print(random_number)

print("J'ai choisi un nombre entre 1 et 30\nA vous de le deviner en 5 tentatives au maximum !")

while player_number != random_number and try_number < 6:
    print(f"Essai no {try_number}")
    try:
        player_number = int(input("Choisissez un nombre: "))
    except ValueError:
        print("Seul une valeur numérique est accepté")
        continue

    if player_number < 1 or player_number > 30:
        print("Le chiffre doit etre entre 1 et 30")
        continue

    print(f"Votre proposition: {player_number}")
    # Check nombre
    if player_number > random_number:
        print("Trop grand")
    elif player_number < random_number:
        print("Trop petit")
    else:
        print(f"Vous avez trouvé en {random_number} en {try_number} essais !")
        break
    try_number += 1
else:
    print("Nombre d'essais dépassé !")
