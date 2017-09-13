class Animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def display_health(self):
        print self.name,"'s health is:", self.health

class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.health = 150
    def pet(self):
        self.health = self.health + 5
        return self
class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.health = 170
    def fly(self):
        self.health = self.health - 10
        return self
    def display_health(self):
        print "I am a Dragon"
        super(Dragon,self).display_health()

dog = Dog("ira").walk().walk().run().display_health()
dragon = Dragon("puff").fly().display_health()




