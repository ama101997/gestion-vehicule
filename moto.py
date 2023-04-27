from vehicle import Vehicle
class Motorcycle(Vehicle):
def _init_(self, make, model, year, color, style):
super()._init_(make, model, year, color)
self.style = style
def _str_(self):
return f"{super()._str_()}, {self.style}"
Partie spécifications techniques
from vehicle_manager import VehicleManager
