class Vehicle:

    def __init__(self, make, year_manufactured, colour="white"):
        self.colour = colour
        self.make = make
        self.year_manufactured = year_manufactured

    def start(self):
        print("Vehicle starting")

    def stop(self):
        print("Vehicle stopping...")


