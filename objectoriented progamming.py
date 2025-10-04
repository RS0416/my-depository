class fruit:
    # class variable
    taste= "sweet"
    def __init__(self, color, name):
        self.name = name
        self.color = color
        
# object creation
apple= fruit("red", "apple")
banana= fruit("green", "banana")
print(apple.name, apple.color)
print(banana.name, banana.color)