import copy
import random


class WrongPositionException(Exception):
    pass


# Creation de la map
# Choisir un nombre de mine et taille de map
taille_map = 10
taille_espace = 3
# mine_number = random.randint(2, 10)
mine_number = 10

# Generer la map
map = [[0] * taille_map for j in range(taille_map)]
value_map = copy.deepcopy(map)
user_map = [["▩"] * taille_map for k in range(taille_map)]


def affiche_map(custom_map=None):
    global map
    if custom_map is not None:
        print("  --- MAP ---")
        print(f"{' ' * taille_espace}{''.join([str(x) for x in range(taille_map)])}")
        print(f"{' ' * taille_espace}{'_' * taille_map}")
        for index_ligne, ligne in enumerate(custom_map):
            print(f"{index_ligne} |", end="")
            for index, char in enumerate(ligne):
                if index == taille_map - 1:
                    print(char)
                else:
                    print(char, end="")
        print(f"{' ' * taille_espace}{'-' * taille_map}")
    else:
        print("--- MAP ---")
        print("".join([str(x) for x in range(taille_map)]))
        for ligne in map:
            for index, char in enumerate(ligne):
                if index == taille_map - 1:
                    print(char)
                else:
                    print(char, end="")
        print("----------")


# Les poser aleatoirement

# Generation
rand_pos = set()
while len(rand_pos) < mine_number:
    rand_pos.add((random.randint(0, taille_map - 1), random.randint(0, taille_map - 1)))

mine_list = list(rand_pos)

# Pose de mine
for pos in mine_list:
    value_map[pos[0]][pos[1]] = "X"


# Passer sur chaque case qui n'est pas une mine et attribuer le chiffre correspondant aux mines sur les cases autour
def check_coords(coord):
    if coord[0] < 0 or coord[0] >= taille_map:
        return False
    elif coord[1] < 0 or coord[1] >= taille_map:
        return False
    else:
        return True


def check_around(y, x):
    coords = [(y + new_y, x + new_x) for new_y in range(-1, 2) for new_x in range(-1, 2)]
    coords.remove((y, x))
    coords = list(filter(check_coords, coords))
    return coords


def get_map_cell(x, y):
    return value_map[y][x]


# Liste de valeur a incrémenter unique
incr_list = set()

complete_pos = []

# Pour chaque position de mine
for mine_coord in mine_list:
    # Je recupere toutes les position correct autour de la mine
    around_mine = check_around(*mine_coord)
    # Je rajoute toutes ces positions dans le set incr_list
    incr_list.update(set(around_mine))
    # Je rajoute toutes ces position dans la liste complete_pos
    complete_pos.extend(around_mine)

for pos in incr_list:
    if value_map[pos[0]][pos[1]] == "X":
        continue
    value_map[pos[0]][pos[1]] = complete_pos.count(pos)

affiche_map(value_map)
affiche_map(user_map)


# Le jeu
def finito():
    for i in range(taille_map):
        for j in range(taille_map):
            if map[i][j] != 'X' and map[i][j] != 0:
                continue
    return ("Finito")


def check_victory():
    global user_map, value_map
    restant = [True if value_map[y][x] == "X" else False for y in range(0, taille_map) for x in range(0, taille_map) if
               user_map[y][x] == "▩"]
    return all(restant)


## Le joueur rentre une position
while not check_victory():
    # Gestion user input
    try:
        x_pos, y_pos = input("Rentrez la position souhaite au format 'x y'").split(" ")
        x_pos, y_pos = int(x_pos), int(y_pos)
        if not check_coords((x_pos, y_pos)):
            raise WrongPositionException()
    except ValueError:
        print("Rentrez deux positions en numérique")
        continue
    except WrongPositionException:
        print(f"Votre position doit se trouver entre 0 et {taille_map}")
        continue

    ## Le systeme verifie
    cell_value = get_map_cell(x_pos, y_pos)
    match cell_value:
        case "X":
            print("Perdu, gros.se nul.le !")
            break
        case 0:
            print("Case sans chiffre")
        case _:
            print("Case avec un chiffre")
            user_map[y_pos][x_pos] = cell_value

# Player input
# Si vide, decouvrir la case
# appel methode recursive checker autour
# prend position x y, recupere les voisins
# pour chaque voisin
# si 0, decouvre la case, et appeller method recursive sur cette cellule
