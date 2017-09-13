class Bike():
    def _init_(self,price,max_speed,miles):
        self.price = 200
        self.max_speed = 25
        self.miles = 0
    def displayInfo(self):
        print "Price is: $" + str(self.price) 
        print "Max Speed:" + str(self.max_speed) + "mph"
        print "Total Miles:" + str(self.miles) + "miles"
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles == 0:
            pass
        else:
            self.miles -= 5
        return self


bike1 = Bike(200,30,0).ride().reverse().ride().reverse.ride().displayInfo()

bike2 = Bike(200,35,0).ride().reverse().ride().reverse().displayInfo()

bike3 = Bike(99,10,0).reverse().reverse().reverse().displayInfo()
