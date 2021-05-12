class Animal:
    
    def __init__(self, name, size="small"):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.name} is a {self.size} {self.whatami()}"

    def whatami(self):
        clazzes = type(self).mro()
        clazzes.pop()  # remove "object" from list

        geneology = ""
        for clazz in clazzes:
            geneology += f"{clazz.__name__} "

        return geneology


yogi = Animal("bear")
print (yogi)
yogi.name = "Yogi"
print(yogi)

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Swimmer():
    def swim(self):
        return f"{self.name} is swimming"
    
class Wolf(Mammal):
    _size = "medium"
    def __init__(self, name):
        super().__init__(name,self._size)


class Bear(Mammal):
    _size = "large"
    def __init__(self, name):
        super().__init__(name,self._size)

class Eagle(Bird):
    _size = "large"
    def __init__(self, name):
        super().__init__(name,self._size)

class Duck(Bird):
    _size = "medium"
    def __init__(self, name):
        super().__init__(name,self._size)

class Frog(Swimmer, Animal):
    _size = "small"
    def __init__(self, name):
        super().__init__(name,self._size)

    def swim(self, depth):
        self.depth = depth
        return f"{super().swim()} at depth of {self.depth}"

class Trout(Swimmer, Animal):
    _size = "small"
    def __init__(self, name):
        super().__init__(name,self._size)

    def swim(self, depth):
        self.depth = depth
        return f"{super().swim()} at depth of {self.depth}"



booboo = Bear("BooBoo")
print(booboo)
booboo.size = "small"

bigBad = Wolf("BigBad")
print(bigBad)

sam = Eagle("Sam")
print(sam)

daffy = Duck("Daffy")
print(daffy)

Kermit = Frog("Kermit")
print(Kermit)
print (Kermit.swim(0))

rainbow = Trout("Rainbow")
print (rainbow)
print(rainbow.swim(1))
