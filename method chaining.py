# method chaining = calling multiple methods sequentially
#   each call performs an action on the same object and returns self

class Car:

    def turnOn(self):
        print("turning on")
        return self

    def drive(self):
        print("driving")
        return self

    def brake(self):
        print("braking")
        return self

    def turn_off(self):
        print("turning off")
        return self

car1 = Car()
car1.turnOn().\
    drive().\
    turn_off()