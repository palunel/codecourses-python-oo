class Game:

    def __init__(self):
        pass

    def escape(self, escape_vehicle):
        escape_vehicle.start()
        print(f"James is escaping in the {escape_vehicle.colour} {escape_vehicle.year_manufactured} {escape_vehicle.make}.")
        escape_vehicle.stop()
