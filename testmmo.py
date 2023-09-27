import mmoguerrier
import mmomage

guerrier = mmoguerrier.Guerrier
mage = mmomage.Mage
""" On appelle les classes guerrier et mage """


class Personnage:
    def __init__(self, pseudo: str, niveau=1, pv=1, initative=1):
        self.pseudo = pseudo
        self.niveau = int(niveau)
        self.pv = int(pv)
        self. initiative = int(initative)

        """ Ici on créé la classe personnage, des valeurs de base sont attribués """

    def perso_joueur(self):
        return f"Pseudo {self.pseudo}, votre niveau : {self.niveau}, votre nombre de pv : {self.pv}, votre niveau d'initiative : {self.initiative}"

    def perso_admin(self):
        return f"Pseudo {self.pseudo}, votre niveau : {self.niveau}, votre nombre de pv : {self.pv}, votre niveau d'initiative : {self.initiative}"

    def attaque(self, perso1, perso2):
        while perso1.pv > 0 and perso2.pv > 0:
            """ Ici on créé une boucle qui ne se finit pas tant que l'un des personnages n'est pas mort """
            if perso1.initiative > perso2.initiative:
                perso2.pv = perso2.pv - perso1.niveau
                print(f"{perso1.pseudo} attaque en premier et inflige {perso1.niveau} dégats, {perso2.pseudo} a {perso2.pv} pv restants.")
                """ Ici, celui qui a l'initiative la plus haute attaque en premier """
                if perso2.pv <= 0:
                    perso2.pv = 0
                    print(f"Combat terminé, {perso1.pseudo} a gagné.")
                    if perso1.pv < perso1.niveau:
                        print(f"Soin activé sur {perso1.pseudo}")
                        perso1.pv = perso1.niveau
                        print(f"{perso1.pseudo} a regagné des pv : {perso1.pv} pv")

                        """
                        Ici on check tout d'abord si le personnage à des pv négatifs, si oui on ramène ses pv à 0 et le combat est terminé
                        Ensuite on regarde si les pv du gagnant sont inférieurs à son propre niveau, si oui on active une fonction de soin
                        qui ramène ses pv à son niveau.
                        """

                else:
                    perso1.pv = perso1.pv - perso2.niveau
                    if perso1.pv <= 0:
                        perso1.pv = 0
                        print(f"Combat terminé, {perso2.pseudo} a gagné.")
                        if perso2.pv < perso2.niveau:
                            print(f"Soin activé sur {perso2.pseudo}")
                            perso2.pv = perso2.niveau
                            print(f"{perso2.pseudo} a regagné des pv : {perso2.pv} pv")

                            """ Ici on refait la même chose que dans le premier if en changeant de personnage """

                    else:
                        print(f"{perso2.pseudo} attaque à son tour et inflige {perso2.niveau}, {perso1.pseudo} a {perso1.pv} pv restants.")

                        """ Enfin quand on a décidé qui a l'initiative la + haute et qu'il attaque, on laisse le second personnage attaquer"""

            elif perso1.initiative < perso2.initiative:
                perso1.pv = perso1.pv - perso2.niveau
                print(f"{perso2.pseudo} attaque en premier et inflige {perso2.niveau} dégats, {perso1.pseudo} a {perso1.pv} pv restants.")
                if perso1.pv <= 0:
                    perso1.pv = 0
                    print(f"Combat terminé, {perso2.pseudo} a gagné.")
                    if perso2.pv < perso2.niveau:
                        print(f"Soin activé sur {perso2.pseudo}")
                        perso2.pv = perso2.niveau
                        print(f"{perso2.pseudo} a regagné des pv : {perso2.pv} pv")
                else:
                    perso2.pv = perso2.pv - perso1.niveau
                    if perso2.pv <= 0:
                        perso2.pv = 0
                        print(f"Combat terminé, {perso1.pseudo} a gagné.")
                    else:
                        print(f"{perso1.pseudo} attaque à son tour et inflige {perso1.niveau}. {perso2.pseudo} a {perso2.pv} pv restants.")
                        """ Le personnage attaque à son tour """
            elif perso1.initiative == perso2.initiative:
                perso2.pv = perso2.pv - perso1.niveau
                perso1.pv = perso1.pv - perso2.niveau
                if perso2.pv <= 0 and perso1.pv > 0:
                    perso2.pv = 0
                    print(f"Combat terminé, {perso1.pseudo} a gagné.")
                    if perso1.pv < perso1.niveau:
                        print(f"Soin activé sur {perso1.pseudo}")
                        perso1.pv = perso1.niveau
                        print(f"{perso1.pseudo} a regagné des pv : {perso1.pv} pv")
                elif perso1.pv <= 0 and perso2.pv > 0:
                    perso1.pv = 0
                    print(f"Combat terminé, {perso2.pseudo} a gagné.")
                    if perso2.pv < perso2.niveau:
                        print(f"Soin activé sur {perso2.pseudo}")
                        perso2.pv = perso2.niveau
                        print(f"{perso2.pseudo} a regagné des pv : {perso2.pv} pv")
                elif perso1.pv <= 0 and perso2.pv <= 0:
                    perso1.pv = 0
                    perso2.pv = 0
                    print("Combat terminé, personne n'a gagné.")
                else:
                    print(f"Ils attaquent en même temps, {perso1.pseudo} a {perso1.pv} pv restants, {perso2.pseudo} a {perso2.pv} pv restants.")

                    """ 
                    Sur cette dernière  partie, on fait un elif dans le cas ou les 2 personnages ont la même initiative,
                    Ils attaquent donc en même temps et celui qui réussit à tuer l'autre a gagné, il y a aussi la 
                    possibilité que les 2 personnages tombent à 0 pv en même temps, les 2 personnages perdent. 
                    """


joueur1 = Personnage("Jax", "12", "105", "70")
joueur2 = Personnage("Sion", "10", "130", "55")
joueur3 = guerrier("Tryndamere", 14)
print(joueur1.perso_joueur())
print(joueur2.perso_admin())
print(joueur3.perso_joueur())
print("")
combat = joueur1.attaque(joueur1, joueur3)
print(combat)

"""
Ici on définit les valeurs des personnages, on print leurs statistiques et enfin on print le combat
"""