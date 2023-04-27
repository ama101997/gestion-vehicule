class Vehicle:
    def __init__(self, vehicle_type, brand, model, year, color, license_plate):
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.license_plate = license_plate

    def __str__(self):
        return f"{self.vehicle_type} {self.brand} {self.model} ({self.color}, {self.year}) immatriculé {self.license_plate}"
