class Animal:
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name} is a {self.size} {self.whatami()}"

    def whatami(self):
        clazzes = type(self).mro()
        clazzes.pop()  # remove "object" from list

        geneology = ""
        for clazz in clazzes:
            geneology += f"{clazz.__name__} "

        return geneology

class Mammal(Animal):
    pass

class Flyer():
    def fly(self):
        return f"{self.name} is flying"

class Climber():
    def climb(self):
        return f"{self.name} is climbing"

class Runner():
    def run(self):
        return f"{self.name} is running"

class Hopper():
    def hop(self):
        return f"{self.name} is hopping"

class Bird(Animal):
    pass

class Swimmer(Animal):
    def swim(self):
        return f"{self.name} is swimming"
    
class Wolf(Mammal,Runner):
    size = "medium"

class Bear(Mammal,Climber,Runner):
    size = "large"

class Eagle(Bird,Flyer):
    size = "large"

class Duck(Bird,Swimmer,Flyer):
    size = "medium"

class Frog(Swimmer, Hopper):
    size = "small"

    def swim(self, depth):
        self.depth = depth
        return f"{super().swim()} at depth of {self.depth}"

class Trout(Swimmer, Animal):
    size = "small"

    def swim(self, depth):
        self.depth = depth
        return f"{super().swim()} at depth of {self.depth}"



booboo = Bear("BooBoo")
print(booboo)
booboo.size = "small"
print(booboo.climb())

bigBad = Wolf("BigBad")
print(bigBad)
print(bigBad.run())

sam = Eagle("Sam")
print(sam)
print(sam.fly())

daffy = Duck("Daffy")
print(daffy)
print(daffy.fly())
print(daffy.swim())

Kermit = Frog("Kermit")
print(Kermit)
print (Kermit.swim(0))
print(Kermit.hop())

rainbow = Trout("Rainbow")
print (rainbow)
print(rainbow.swim(1))
