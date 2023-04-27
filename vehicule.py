class Vehicle:
def _init_(self, make, model, year, color):
self.make = make
self.model = model
self.year = year
self.color = color
def _str_(self):
return f"{self.year} {self.make} {self.model} ({self.color})"
