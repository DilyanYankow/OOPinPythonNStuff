from car import Car

car1 = Car("Chevy", "Corvette", 2021, "blue")
car2 = Car("Ford", "Mustang", 2022, "red")
print(car1.make)
print(car1.model)
print(car1.color)
print(car1.year)

Car.wheels = 2      #changes wheels of all cars

print(car1.wheels)

car1.drive()
car1.stop()