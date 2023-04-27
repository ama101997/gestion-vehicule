from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from bus import Bus
from subway import Subway
from vehicle_stats import VehicleStats
def main():
# Créer quelques véhicules
car1 = Car("Toyota", "Corolla", "2018", "Blanc", 4, "Essence")
car2 = Car("Honda", "Civic", "2020", "Noir", 4, "Essence")
motorcycle1 = Motorcycle("Kawasaki", "Ninja", "2021", "Vert", "Sportive")
bus1 = Bus("Volvo", "XC90", "2019", "Rouge", 50)
subway1 = Subway("Bombardier", "Movia", "2020", "Argenté", 1200)
# Créer une liste de véhicules
vehicles = [car1, car2, motorcycle1, bus1, subway1]
# Créer un objet VehicleStats pour afficher les statistiques
vehicle_stats = VehicleStats(vehicles)
# Afficher le nombre total de véhicules
print(f"Nombre total de véhicules: {vehicle_stats.get_total_vehicles()}")
# Afficher le nombre de véhicules par type
print(f"Nombre de voitures: {vehicle_stats.get_vehicle_count_by_type('Car')}")
print(f"Nombre de motos: {vehicle_stats.get_vehicle_count_by_type('Motorcycle')}")
print(f"Nombre de bus: {vehicle_stats.get_vehicle_count_by_type('Bus')}")
print(f"Nombre de métros: {vehicle_stats.get_vehicle_count_by_type('Subway')}")
# Afficher le nombre de véhicules par couleur
print(f"Nombre de voitures blanches: {vehicle_stats.get_vehicle_count_by_color('Blanc')}")
print(f"Nombre de motos vertes: {vehicle_stats.get_vehicle_count_by_color('Vert')}")
if _name_ == "_main_":
main()
