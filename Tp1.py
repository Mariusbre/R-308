import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Cercle:
    def __init__(self, rayon=3.0):
        self.centre = Point()
        self.rayon = rayon

    def __init__(self, centre, rayon=3.0):
        self.centre = centre
        self.rayon = rayon

    def diametre(self):
        return 2 * self.rayon

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def surface(self):
        return self.rayon * self.rayon * math.pi


point_centre = Point(2.0, 3.0)
cercle = Cercle(4.0)

diametre_cercle = cercle.diametre()

print(f"Diamètre cercle : {diametre_cercle}")

périmètre = cercle.perimetre()
print(f"Périmètre : {périmètre}")

surface = cercle.surface()
print(f"Surface : {surface}")


class Rectangle:
    def __init__(self, longueur=1, hauteur=1):
        self.point = Point
        self.longueur = longueur
        self.hauteur = hauteur