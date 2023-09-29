import pickle


class Vehicule:
    def __init__(self, marque, roues, modele):
        self.__marque = marque
        self.__roues = roues
        self.__modele = modele

    @property
    def marque(self):
        return self.__marque

    @property
    def roues(self):
        return self.__roues

    @property
    def modele(self):
        return self.__modele

    def __str__(self):
        return f"Marque : {self.__marque}\nRoues : {self.__roues}\nModele : {self.__modele}"


class Voiture(Vehicule):
    def __init__(self, marque, roues, modele, options):
        super().__init__(marque, roues, modele)
        self.__options = options

    @property
    def options(self):
        return self.__options

    def __str__(self):
        return f"Marque : {self.marque}\nModèle : {self.modele}\nRoues : {self.roues}\nOptions : {self.__options}"


class Moto(Vehicule):
    def __init__(self, marque, modele, roues, puissance):
        super().__init__(marque, roues, modele)
        self.__puissance = puissance

    @property
    def puissance(self):
        return self.__puissance

    def __str__(self):
        return f"Marque : {self.marque}\nModèle : {self.modele}\nRoues : {self.roues}\nPuissance : {self.__puissance}ch"


class Catalogue:
    def __init__(self):
        self.__vehicules = []

    def ajouter_vehicule(self, vehicule):
        self.__vehicules.append(vehicule)

    def get_vehicules(self):
        return self.__vehicules

    def __str__(self):
        return "\n".join([str(vehicule) for vehicule in self.__vehicules])


audi = Voiture("Audi", "4", "A3", "ABS")
mercedes = Voiture("Mercedes", "4", "Classe A", "Toit ouvrant")
honda = Moto("Honda", "2", "CBF 600 S", "78")

catalogue = Catalogue()
catalogue.ajouter_vehicule(audi)
catalogue.ajouter_vehicule(mercedes)
catalogue.ajouter_vehicule(honda)

with open("catalogue.pkl", "wb") as file:
    pickle.dump(catalogue, file)

with open("catalogue.pkl", "rb") as file:
    catalogue_charge = pickle.load(file)

print("\nContenu du catalogue chargé depuis le fichier:")
print(catalogue_charge)