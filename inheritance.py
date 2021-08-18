# Multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:

    alive = True

class Animal(Organism):

    def eat(selfself):
        print("Animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")

dog1 = Dog()
# print(dog1.alive)
dog1.eat()
if dog1.alive == True:
    print("Dog is alive!")
