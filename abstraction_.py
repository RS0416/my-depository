from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("Humans can talk and walk.")


class dog(animal):
    def move(self):
        print("Dogs can bark")

class snake(animal):
    def move(self):
        print("Snakes can slither.")

obj1= human()
obj1.move()
obj2= snake()
obj2.move()
obj3= dog()
obj3.move()