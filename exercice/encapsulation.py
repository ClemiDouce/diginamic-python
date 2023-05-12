# 1
class Rectangle:
    nom = "rectangle"
    longueur = 0
    largeur = 0

    def __init__(self, longueur=0, largeur=0):
        self.longueur = longueur
        self.largeur = largeur

    def affiche(self):
        print(f"Nom: {self.nom} / Longueur: {self.longueur} / Largeur: {self.largeur}")

    def surface(self):
        print(f"Surface: {self.longueur * self.largeur}")


class Carre(Rectangle):
    nom = "carré"


rec = Rectangle()
carre = Carre()

rec.affiche()
carre.affiche()


# 2

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, p1, p2, p3, p4):
        self.orig = Point(p1, p2)
        self.extrem = Point(p3, p4)

    def affiche(self):
        print(f"Origine : [x: {self.orig.x}, y:{self.orig.y}] | Extremité : [x: {self.extrem.x}, y:{self.extrem.y}]")


seg = Segment(10, 20, 100, 200)
seg.affiche()


# 3
def fabriquer_creer_plus():
    pass
