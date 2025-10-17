class point:
    def __init__ (self, value, side):
        self.value= value
        self.side= side
    def __str__ (self):
        return "({0}, {1})".format (self.value, self.side)
obj1= point(400, "  6th Side")
print(obj1)