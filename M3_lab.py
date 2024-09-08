class Vehicle():
    def __init__(self,vehicleType):
        self.vehicleType = vehicleType
        

class Automobile(Vehicle):
    def __init__(self, vehicleType, year, make, model, doors, roof):
        valid_doors = ["2", "4"]
        valid_roof = ["solid", "sun roof"]
        
        year = input("Year: ")
        make = input("Make: ")
        model = input("Model: ")
        doors = self.error_check(input("Doors (2 or 4): "), valid_doors)
        roof = self.error_check(input("Roof (solid or sun roof):"),)
        
        
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return f"Vehicle type: {self.vehicleType}\nYear: {self.year}\nMake: {self.make}\n"

    def error_check(self, trait, check):
        if self.trait not in valid_doors


vehicleType = "car"

if vehicleType == "car":
    myVehicle = Automobile(vehicleType)

myVehicle()