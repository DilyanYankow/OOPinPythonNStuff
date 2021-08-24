class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle, color):
    vehicle.color = color

mot1 = Motorcycle()

change_color(mot1, "red")
print(mot1.color)

car1 = Car()
car2 = Car()

print(car1.color)
print(car2.color)

change_color(car1, "red")
change_color(car2, "white")


print(car1.color)
print(car2.color)
