class Mage:
    def __init__(self, pseudo: str, niveau: int):
        self.pv = niveau * 5 + 10
        self.pseudo = pseudo
        self.niveau = niveau
        self.initiative = niveau * 6 + 4
        self.mana = niveau * 5

    def perso_joueur(self):
        return f"Pseudo {self.pseudo}, votre niveau : {self.niveau}, votre nombre de pv : {self.pv}, votre niveau d'initiative : {self.initiative}, votre mana : {self.mana}"

    def perso_admin(self):
        return f"Pseudo {self.pseudo}, votre niveau : {self.niveau}, votre nombre de pv : {self.pv}, votre niveau d'initiative : {self.initiative}, votre mana : {self.mana}"