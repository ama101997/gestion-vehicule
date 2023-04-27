class Vehicule:
    nom_application = "Gestion des véhicules"

    def __init__(self, modele: str, nb_roues: int, couleurs: list, plaque: str, type_vehicule: str, jantes: bool = False):
        self.modele = modele
        self.nb_roues = nb_roues
        self.couleurs = couleurs
        self.plaque = plaque
        self.type_vehicule = type_vehicule
        self.jantes = jantes


        super().__init__(modele, nb_roues, couleurs, plaque, "Voiture")
        self.marque = marque
        self.annee = annee
        Voiture.nb_voitures += 1

class Moto(Vehicule):
    nb_motos = 0

    def __init__(self, modele: str, nb_roues: int, couleurs: list, plaque: str, marque: str, annee: int, sidecar: bool = False):
        super().__init__(modele, nb_roues, couleurs, plaque, "Moto")
        self.marque = marque
        self.annee = annee
        self.sidecar = sidecar
        Moto.nb_motos += 1

class Bus(Vehicule):
    nb_bus = 0

    def __init__(self, modele: str, nb_roues: int, couleurs: list, plaque: str, nb_places: int, annee: int):
        super().__init__(modele, nb_roues, couleurs, plaque, "Bus")
        self.nb_places = nb_places
        self.annee = annee
        Bus.nb_bus += 1

    
    def set_nb_roues(self, nb_roues):
        self.nb_roues = nb_roues
        
    def set_plaque_immatriculation(self, plaque_immatriculation):
        self.plaque_immatriculation = plaque_immatriculation
        
    def set_type_vehicule(self, type_vehicule):
        self.type_vehicule = type_vehicule
        
    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee}) de couleur {self.couleur}"
        
        
