class vehicle:
    brand= "audi"
    def __init__ (self, name, brand):
        self.name= name
        self.brand= brand
    def display(self):
        print("the brand of the car is ", self.brand)

mercedes= vehicle("kookee=", "Mercedes Benz")
audi= vehicle("keekaah=", "Audi")
print(mercedes.name, mercedes.brand)
print(audi.name, audi.brand)
audi.display