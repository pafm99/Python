class Car():
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        
    def tax(self):
        if self.price > 10000:
            self.tax = self.price * 0.15
        else: self.tax = self.price * 0.12
        return self
    def displayAll(self):
        print "The Price is:", self.price
        print "The Max speed is:", self.speed
        print "The tank of fuel is:", self.fuel
        print "The total miles driven is:", self.mileage
        print "The tax is:", self.tax
        return self

car1 = Car(2000,35,"Full",15).tax().displayAll()
print "///"
car2 = Car(2000,5,"Not Full",105).tax().displayAll()
print "///"
car3 = Car(2000,15,"Kind of Full",95).tax().displayAll()
print "///"
car4 = Car(2000,25,"Full",25).tax().displayAll()
print "///"
car5 = Car(2000,35,"Empty",15).tax().displayAll()

