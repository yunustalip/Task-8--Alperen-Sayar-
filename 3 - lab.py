class Animal(object):

    def __init__(self, name):
        self.name = name
        self.health = 50
    
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print("{}'s health is {}".format(self.name, self.health))
        return self

class Dinosaur(Animal):

    def __init__(self, name):
        super(Dinosaur, self).__init__(name)
        self.health = 150

    def dis(self):
        super(Dinosaur, self).displayHealth()
        print("I am a Dinosaur")
        return self


class Orkinos(Animal):
    
    def __init__(self, name):
        super(Orkinos, self).__init__(name)
        self.health = 100

    def swim(self):
        self.health -= 3
        return self

    def dis(self):
        super(Orkinos, self).displayHealth()
        print("I am a Orkinos")
        return self


class Eagle(Animal):
    
    def __init__(self, name):
        super(Eagle, self).__init__(name)
        self.health = 60

    def fly(self):
        self.health -= 10
        return self

    def dis(self):
        super(Eagle, self).displayHealth()
        print("I am a Eagle")
        return self

test = Animal("test")
test.walk().walk().walk().run().run().displayHealth()

test2 = Dinosaur("test2")
test2.walk().walk().walk().run().run().displayHealth()

test3 = Eagle("test3")
test3.fly().dis()

test4 = Orkinos("test4")
test4.swim().dis()
