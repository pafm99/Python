class Products():
    def __init__(self,price,item_name,weight,brand,cost,status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    def sell(self):
        self.status = "sold"
    def return_reason(self,return_reason):
        if return_reason == "defective":
            self.price = 0
        elif return_reason =="inbox_open":
            self.price = self.price - self.price * 0.20
        elif return_reason == "inbox":
            self.status = "For Sale"
        return self
    def tax(self,tax):
        self.price = self.price + self.price * tax
        return self
    def display(self):
        print "The price is: $", self.price
        print "The product name is: ", self.item_name
        print "The product weight is: ", self.weight
        print "The cost of the product is: ",self.cost
        print "This item is: ", self.status
        return self
product1 = Products(10.00,"shoes",5,"nike",7,"sold").tax(.10).return_reason("inbox").display()

        
