from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, make, year_manufactured, engine, colour):
        super(Car, self).__init__(make, year_manufactured, colour)
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

