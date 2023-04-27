class Application:
def _init_(self):
self.app_name = "Gestionnaire de véhicules"
self.vehicle_manager = VehicleManager()
def run(self):
print(f"Bienvenue dans l'application {self.app_name}!")
while True:
print("Que voulez-vous faire?")
print("1 - Ajouter un véhicule")
print("2 - Modifier un véhicule")
print("3 - Supprimer un véhicule")
print("4 - Afficher les statistiques")
print("5 - Quitter")
choice = input("Entrez votre choix: ")
if choice == "1":
self.add_vehicle()
elif choice == "2":
self.modify_vehicle()
elif choice == "3":
self.delete_vehicle()
elif choice == "4":
self.display_statistics()
elif choice == "5":
print("Merci d'avoir utilisé l'application!")
break
else:
print("Choix invalide. Veuillez réessayer.")
def add_vehicle(self):
print("Ajout d'un véhicule:")
vehicle_type = input("Type de véhicule (car, motorcycle, bus, subway): ")
make = input("Marque: ")
model = input("Modèle: ")
year = input("Année: ")
color = input("Couleur: ")
if vehicle_type == "car":
num_doors = int(input("Nombre de portes: "))
fuel_type = input("Type de carburant: ")
self.vehicle_manager.add_car(make, model, year, color, num_doors, fuel_type)
elif vehicle_type == "motorcycle":
style = input("Style: ")
self.vehicle_manager.add_motorcycle(make, model, year, color, style)
elif vehicle_type == "bus":
capacity = int(input("Capacité: "))
self.vehicle_manager.add_bus(make, model, year, color, capacity)
elif vehicle_type == "subway":
capacity = int(input("Capacité: "))
self.vehicle_manager.add_subway(make, model, year, color, capacity)
else:
print("Type de véhicule invalide. Veuillez réessayer.")
def modify_vehicle(self):
print("Modification d'un véhicule:")
vehicle_id = int(input("ID du véhicule à modifier: "))
vehicle = self.vehicle_manager.get_vehicle_by_id(vehicle_id)
if vehicle is None:
print("ID de véhicule invalide. Veuillez réessayer.")
return
print(f"1 - Modifier la marque (actuel: {vehicle.make})")
print(f"2 - Modifier le modèle (actuel: {vehicle.model})")
print(f"3 - Modifier l'année (actuel: {vehicle.year})")
print(f"4 - Modifier la couleur (actuel: {vehicle.color})")
if isinstance(vehicle, Car):
print(f"5 - Modifier le nombre de portes (actuel: {vehicle.num_doors})")
print(f"6 - Modifier le type de carburant (actuel: {vehicle.fuel_type})")
elif isinstance(vehicle, Motorcycle):
print(f"5 - Modifier le style (actuel: {vehicle.style})")
elif isinstance(vehicle, Bus) or isinstance(vehicle
