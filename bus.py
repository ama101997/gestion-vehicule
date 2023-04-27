class Moto(Vehicule):
    nb_motos = 0

    def __init__(self, modele: str, nb_roues: int, couleurs: list, plaque: str, marque: str, annee: int, sidecar: bool = False):
        super().__init__(modele, nb_roues, couleurs, plaque, "Moto")
        self.marque = marque
        self.annee = annee
        self.sidecar = sidecar
        Moto.nb_motos += 1