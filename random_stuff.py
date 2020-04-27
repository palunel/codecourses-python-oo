class Vehicle:

    def __init__(self, colour, make, year_manufactured):
        self.colour = colour
        self.make = make
        self.year_manufactured = year_manufactured

    def start(self):
        print("Vehicle starting")

    def stop(self):
        print("Vehicle stopping...")


class Car(Vehicle):

    def __init__(self, colour, make, year_manufactured, engine):
        super(Car, self).__init__(colour, make, year_manufactured)
        self.engine = electric_engine

    def start(self):
        self.engine.start()
        print("Car Starting...")


    def accelerate(self):
        print("Car accelerating...")
        return acceleration_confirmation

class Boat(Vehicle):

    def __init__(self, colour, make, year_manufactured, engine):
        super(Boat, self).__init__(colour, make, year_manufactured)
        self.engine = outboard_motor

    def start(self):
        self.engine.start()
        print("Boat starting...")

    def accelerate(self):
        print("Boat accelerating...")

