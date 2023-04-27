from vehicle import Vehicle
from vehicle_registry import VehicleRegistry

def launch_application():
    print("Bienvenue dans l'application de gestion de véhicules !")
    registry = VehicleRegistry()
    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Ajouter un véhicule")
        print("2. Modifier un véhicule")
        print("3. Supprimer un véhicule")
        print("4. Afficher des statistiques")
        print("5. Quitter l'application")
        choice = input("> ")
        if choice == "1":
            registry.add_vehicle()
        elif choice == "2":
            registry.modify_vehicle()
        elif choice == "3":
            registry.remove_vehicle()
        elif choice == "4":
            registry.show_statistics()
        elif choice == "5":
            break
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    launch_application()
