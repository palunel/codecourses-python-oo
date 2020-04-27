class Car:

    def __init__(self, colour, make, year_manufactured, engine):
        self.colour = colour
        self.make = make
        self.year_manufactured = year_manufactured
        self.engine = engine

    def start(self):
        print("Car Starting...")

    def stop(self):
        print("Car Stopping...")

    def accelerate(self):
        print("Car accelerating...")

    def brake(self):
        print("Car braking...")
