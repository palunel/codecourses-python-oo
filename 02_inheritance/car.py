from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, colour, make, year_manufactured, engine):
        super(Car, self).__init__(colour, make, year_manufactured)
        self.engine = engine

    # Overriding Vehicle's implementation of start
    def start(self):
        print("Car starting...")

    def stop(self):
        print("Car stopping...")

    # Extending the Vehicle class with new functionality
    def accelerate(self):
        print("Car accelerating...")

    def brake(self):
        print("Car braking...")

