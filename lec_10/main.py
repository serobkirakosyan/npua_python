from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, model, color, year, maxSpeed):
        super().__init__(model, year, color)
        self.maxSpeed = maxSpeed


class Plane(Vehicle):
    def __init__(self, model, color, year, numberOfPlaces):
        super().__init__(model, color, year)
        self.numberOfPlaces = numberOfPlaces


class Boat(Vehicle):
    def __init__(self, model, color, year, maxVeight):
        super().__init__(model, color, year)
        self.maxVeight = maxVeight


class RaceCar(Car):
    def __init__(self, model, color, year, maxSpeed, tireLength):
        super().__init__(model, color, year, maxSpeed)
        self.tireLength = tireLength


car = Car("BMW", "Black", 2007, 260)
plane = Plane("Boeing", "White", 2015, 120)
boat = Boat("AcuaTec", "Blue", 2020, 500)
raceCar = RaceCar("MersedesBenz", "Black", 2023, 350, 325)

print(car)
print(plane)
print(boat)
print(raceCar)