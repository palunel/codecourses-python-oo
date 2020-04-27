from vehicle import Vehicle


class Boat(Vehicle):
    def __init__(self, colour, make, year_manufactured, engine):
        super(Boat, self).__init__(colour, make, year_manufactured)
        self.engine = engine

    def start(self):
        print("Boat starting...")

    def accelerate(self):
        print("Boat accelerating...")

