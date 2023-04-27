from vehicle import Vehicl
class Car(Vehicle):
def _init_(self, make, model, year, color, num_doors, fuel_type):
super()._init_(make, model, year, color)
self.num_doors = num_doors
self.fuel_type = fuel_type
def _str_(self):
return f"{super()._str_()}, {self.num_doors} portes, {self.fuel_type}"
