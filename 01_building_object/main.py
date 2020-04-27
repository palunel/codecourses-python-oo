from car import Car

pauls_vw = Car(colour="red", make="VW", year_manufactured=2010, engine="V6")

pauls_vw.start()
pauls_vw.accelerate()
pauls_vw.brake()
pauls_vw.stop()

print(f"The colour of my {pauls_vw.make} is {pauls_vw.colour}")

pauls_vw.colour = "blue"

print(f"The colour of my {pauls_vw.make} is {pauls_vw.colour}")
