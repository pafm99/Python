#PRINT A CLASS OF SUPER HERO
#HAS NAME
#CITY
#POWER

class SuperHero(object):
    def __init__(self, name,city,power):
        self.name = name
        self.city = city
        self.power = power
SuperPaul = SuperHero("supersonic", "seattle", "superspeed")#instance of class

class Villan(object):
    def __init__(self, name, city, power):
        self.name = name
        self.city = city
        self.power = power

villa_ian = Villan("Villan_ian", "everett", "sopercoder") # instance of class

class SideKick(object):
    def __init__(self, name, city,  power):
        self.name = name
        self.city = city
        self.power
sidekick1 = SideKick("joe", "auburn","super_thinking") #instance of a class


