class parent:
    def __init__(self, eyes,aggresive):
        self.eyes= eyes
        self.aggresive= aggresive
    
    def display(self):
        print("your eye colour is", self.eyes)
        print("your aggresiveness is", self.aggresive)

class child(parent):
    def __init__ (self, eyes, height, aggresive):
       self.height= height
       super().__init__(eyes, aggresive)
    def mydisplay(self):
        print("your height is", self.height)
obj= child("blue", 4, True)
obj.mydisplay()
obj.display()