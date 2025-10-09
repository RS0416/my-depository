class dog:
    breed= "shitzu"
    def __init__(self, name, breed):
        self.name= name
        self.breed= breed
    def display(self):
        print("the breed of the dog is", self.breed)

shitzu= dog("pepsi", "shitzu")
goldret= dog("heehaa", "goldret")
print(shitzu.name, shitzu.breed)
print(goldret.name, goldret.breed)
shitzu.display