class Vehicle():
    def __init__(self,vehicleType):
        self.vehicleType = vehicleType
        

class Automobile(Vehicle):
    def __init__(self, vehicleType, year, make, model, doors, roof): 
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return f"Vehicle type: {self.vehicleType}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nDoors: {self.doors}\nRoof: {self.roof}"

## App start
def error_check(trait, check):
    if trait in check:
        return True
    else:
        return False

vehicleType = "car"

if vehicleType == "car":

    #for error checking
    valid_doors = ["2", "4"]
    valid_roof = ["solid", "sun roof"]

    doors = ""
    roof = ""
        
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Doors (2 or 4): ")
    # check for validity
    while not error_check(doors, valid_doors):
        doors = input("Doors (2 or 4): ")
        
    roof = input("Roof (solid or sun roof): ")
    while not error_check(roof, valid_roof):
        roof = input("Roof (solid or sun roof): ")
        
    myVehicle = Automobile(vehicleType, year, make, model, doors, roof)
    
print(myVehicle)