class vehicle:
    def __init__ (self, shape, colour):
        self.shape= shape
        self.colour= colour

    def display(self):
        print("your shape is ", self.shape)
        print("your colour is ", self.colour)

class bus(vehicle):
    def __init__ (self, shape, colour, size):
        self.size= size
        super().__init__(shape, colour)
    def mydisplay(self):
        print("your size is ", self.size)

obj= bus("square", True, 4)
obj.display()
obj.mydisplay()