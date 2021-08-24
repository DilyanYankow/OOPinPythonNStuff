# Abstract prevent a user from creating an object of that class
# and compels a user to override abstract methods in a child class

# Abstract class = a class which contains one or more abstract methods!
# Abstract method = a method that has a declaration but does not have implementation
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

class Car:

    def go(self):
        print("Car goes brr")

class Motorcycle(Vehicle):
    def go(self):
        print("Motorcycle goes brr")

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()