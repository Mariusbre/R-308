class Guerrier:
    def __init__(self, pseudo: str, niveau: int):
        self.pv = niveau * 8 + 4
        self.pseudo = pseudo
        self.niveau = niveau
        self.initiative = niveau * 4 + 6

    def perso_joueur(self):
        return f"Pseudo {self.pseudo}, votre niveau : {self.niveau}, votre nombre de pv : {self.pv}, votre niveau d'initiative : {self.initiative}"

    def perso_admin(self):
        return f"Pseudo {self.pseudo}, votre niveau : {self.niveau}, votre nombre de pv : {self.pv}, votre niveau d'initiative : {self.initiative}"
