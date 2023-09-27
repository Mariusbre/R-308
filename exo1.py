def addition(a: int, b: int) -> int:
    return a + b


def fonction1(a: int, b:int) -> int:
    if a > b:
        return a
    else: return b


def fonction2(a :int):
    if a > 10:
        print("supérieur a 10")


def fonction3(*args):
    return max(args)


print(fonction3(max(1,3,2)))


def fonction4(*args):
    t = [args]
    return sorted(args)
print(fonction4(1,2,3,4,5,6))


class Tasse:
    matiere : str = "céramique"

    def __init__(self, couleur: str, contenance: int, marque: str):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque

    def __str__(self):
        return (f"la tasse de matière {self.matiere} de couleur { self.couleur}  et de marque { self.marque} a une contenance de { self.contenance} ml")

    