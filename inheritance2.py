class Predator:
    def hunt(self):
        print("hunting")

class Prey:
    def flee(self):
        print("fleeing")

class Rabbit(Prey):
    pass

class Wolf(Predator):
    pass

class Fish(Prey, Predator):
    pass

fish1 = Fish()

fish1.flee()
