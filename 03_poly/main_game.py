from game import Game
from car import Car
from boat import Boat
from server import Server

import random

bond = Game()

escape_car = Car(make="VW", year_manufactured=2017, engine="Small", colour="Blue")
escape_boat = Boat(make="Regal", year_manufactured=1997, engine="Small", colour="Black")
game_server = Server(name="Game Server", address="127.0.0.1", make="Dell", year_manufactured=2019)
vehicle = random.choice([escape_boat, escape_car, game_server])

bond.escape(vehicle)


