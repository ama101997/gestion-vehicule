class VehiculeManager:
    def __init__(self):
        self.vehicules = [] # La liste de tous les véhicules enregistrés
    
    def run(self):
        print("Bienvenue dans l'application de gestion des véhicules!")
        while True:
            print("Que voulez-vous faire ?")
            print("1. Ajouter un véhicule")
            print("2. Supprimer un véhicule")
            print("3. Modifier un véhicule")
            print("4. Afficher des statistiques")
            print("5. Quitter l'application")
            
            choix = input("Entrez votre choix: ")
            
            if choix == "1":
                self.ajouter_vehicule()
            elif choix == "2":
                self.supprimer_vehicule()
            elif choix == "3":
                self.modifier_vehicule()
            elif choix == "4":
                self.afficher_statistiques()
            elif choix == "5":
                self.quitter_application()
            else:
                print("Choix invalide. Veuillez réessayer.")
    
    def ajouter_vehicule(self):
        # Ajouter un véhicule à la liste des véhicules
        pass
    
    def supprimer_vehicule(self):
        # Supprimer un véhicule de la liste des véhicules
        pass
    
    def modifier_vehicule(self):
        # Modifier un véhicule de la liste des véhicules
        pass
    
    def afficher_statistiques(self):
        # Afficher des statistiques sur les véhicules enregistrés
        pass
    
    def quitter_application(self):
        print("Au revoir!")
        exit()
