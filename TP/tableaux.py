import random

taille_classe = 30
nombre_note = 10

tab_etudiant = [[random.randint(0, 21) for _ in range(nombre_note)] for _ in range(taille_classe)]


def moyenne_etudiant(eleve):
    return round(sum(eleve) / len(eleve), 2)


def get_tab_moyenne(promotion):
    return [moyenne_etudiant(eleve) for eleve in promotion]


def moyenne_classe(promotion):
    return sum(get_tab_moyenne(promotion))


def get_better_student(promotion):
    prom_notes = get_tab_moyenne(promotion)
    return max(prom_notes)


print(moyenne_classe(tab_etudiant))
