class Vehicle:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color


    def __str__(self):
        return f"{self.model} {self.year} {self.color}"