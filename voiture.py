class Voiture(Vehicule):
    nb_voitures = 0

    def __init__(self, modele: str, nb_roues: int, couleurs: list, plaque: str, marque: str, annee: int):
        super().__init__(modele, nb_roues, couleurs, plaque, "Voiture")
        self.marque = marque
        self.annee = annee
        Voiture.nb_voitures += 1