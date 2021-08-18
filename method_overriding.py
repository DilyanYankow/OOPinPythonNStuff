class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating carrots.")

rabbit1 = Rabbit()
rabbit1.eat()