class Personnage:
    def __init__(self, pseudo: str, niveau=1, pv=1, initative=1):
        self.pseudo = pseudo
        self.niveau = int(niveau)
        self.pv = int(pv)
        self. initiative = int(initative)

    def perso_joueur(self):
        return f"Pseudo {self.pseudo}, votre niveau : {self.niveau}, votre nombre de pv : {self.pv}, votre niveau d'initiative : {self.initiative}"

    def perso_admin(self):
        return f"Pseudo {self.pseudo}, votre niveau : {self.niveau}, votre nombre de pv : {self.pv}, votre niveau d'initiative : {self.initiative}"

    def attaque(self, perso1, perso2):
        while perso1.pv != 0 or perso2.pv != 0:
            if perso1.initiative > perso2.initiative:
                perso2.pv = perso2.pv - joueur1.niveau
                if perso2.pv <= 0:
                    perso2.pv = 0
                    print(f"combat terminé, {perso1.pseudo} a gagné")
                else:
                    perso1.pv = perso1.pv - perso2.niveau
                    print(f"{perso2.pseudo} attaque à son tour et inflige {perso2.niveau}, {perso1.pseudo} à {perso1.pv} pv restant")
                return f"{perso1.pseudo} attaque en premier, {perso2.pseudo} à {perso2.pv} pv restant"

            elif perso1.initiative < perso2.initiative:
                perso1.pv = perso1.pv - perso2.niveau
                if perso1.pv <= 0:
                    perso1.pv = 0
                    print(f"combat terminé, {perso2.pseudo} a gagné")
                else:
                    perso2.pv = perso2.pv - perso1.niveau
                    print(f"{perso1.pseudo} attaque à son tour et inflige {perso1.niveau}, {perso2.pseudo} à {perso2.pv} pv restant")
                return f"{perso2.pseudo} attaque en premier, {perso1.pseudo} à {perso1.pv} pv restant"
            elif perso1.initiative == perso2.initiative:
                perso2.pv = perso2.pv - joueur1.niveau
                perso1.pv = perso1.pv - perso2.niveau
                return f"Ils attaquent en même temps, {perso1.pseudo} à {perso1.pv} pv restant, {perso2.pseudo} à {perso2.pv} pv restant"


joueur1 = Personnage("Jax", "21", "75", "40")
joueur2 = Personnage("Sion", "15", "105", "47")
print(joueur1.perso_joueur())
print(joueur2.perso_admin())
print("")
combat = joueur1.attaque(joueur1,joueur2)
print(combat)
