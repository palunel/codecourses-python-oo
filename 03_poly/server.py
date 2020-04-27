class Server:

    def __init__(self, name, address, make, year_manufactured):
        self.name = name
        self.address = address
        self.make = make
        self.year_manufactured = year_manufactured
        self.colour = "Vanta Black"

    def start(self):
        print(f"The {self.make} server, {self.name}, is starting at {self.address}...")

    def stop(self):
        print(f"{self.name} running at {self.address} has stopped.")