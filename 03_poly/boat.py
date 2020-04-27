from vehicle import Vehicle


class Boat(Vehicle):
    def __init__(self, make, year_manufactured, engine, colour):
        super(Boat, self).__init__(make, year_manufactured, colour)
        self.engine = engine

    def start(self):
        print("Boat starting...")

