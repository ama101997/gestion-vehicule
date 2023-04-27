class VehiculeApp:
    def __init__(self, nom):
        self.nom = nom
        self.vehicules = []

    def lancer(self):
        print(f"Bienvenue dans l'application {self.nom} !")

        while True:
            choix = input("Que voulez-vous faire ? (ajouter/afficher/supprimer/modifier/quitter) ")

            if choix == "ajouter":
                self.ajouter_vehicule()
            elif choix == "afficher":
                self.afficher_vehicules()
            elif choix == "supprimer":
                self.supprimer_vehicule()
            elif choix == "modifier":
                self.modifier_vehicule()
            elif choix == "quitter":
                break
            else:
                print("Choix invalide, veuillez réessayer.")

        print(f"Merci d'avoir utilisé l'application {self.nom} !")

    def ajouter_vehicule(self):
        type_vehicule = input("Quel est le type de véhicule ? (voiture/moto/autobus/métro) ")

        if type_vehicule == "voiture":
            vehicule = Voiture(input("Marque : "), input("Modèle : "), int(input("Année : ")), input("Couleur : "), input("Plaque minéralogique : "))
        elif type_vehicule == "moto":
            vehicule = Moto(input("Marque : "), input("Modèle : "), int(input("Année : ")), input("Couleur : "), int(input("Cylindrée : ")))
        elif type_vehicule == "autobus":
            vehicule = Autobus(input("Marque : "), input("Modèle : "), int(input("Année : ")), input("Couleur : "), int(input("Capacité : ")))
        elif type_vehicule == "métro":
            vehicule = Metro(input("Marque : "), input("Modèle : "), int(input("Année : ")), input("Couleur : "), int(input("Nombre de wagons : ")))
        else:
            print("Type de véhicule invalide, veuillez réessayer.")
            return

        self.vehicules.append(vehicule)
        print(f"{type_vehicule.capitalize()} ajouté avec succès !")

    def afficher_vehicules(self):
        if len(self.vehicules) == 0:
            print("Aucun véhicule enregistré.")
            return

        print("Liste des véhicules :")
        for vehicule in self.vehicules:
            print(f"- {vehicule}")

    def supprimer_vehicule(self):
        if len(self.vehicules) == 0:
            print("Aucun véhicule à supprimer.")
            return

        immatriculation = input("Quelle est la plaque minéralogique du véhicule à supprimer ? ")

        for i, vehicule in enumerate(self.vehicules):
            if isinstance(vehicule, Voiture) and vehicule.immatriculation == immatriculation:
                del self.vehicules[i]
                print("Voiture supprimée avec succès.")
                return
            elif isinstance(vehicule, Moto) and vehicule.immatriculation == immatriculation:
                del self.vehicules[i
