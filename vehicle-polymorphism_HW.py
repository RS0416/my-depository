from abc import ABC, abstractmethod
class bmw(ABC):
    def move(self):
        pass

class ferrari(bmw):
    def move(self):
        print(" the ferrari can be fast.")

class racers(bmw):
    def move(self):
        print("the racers can move fastly")

class tough_vehs(bmw):
    def move(self):
        print("the tough_vehs can be tough and strong")

obj1=ferrari()
obj1.move()
obj2= racers()
obj2.move()
obj3=tough_vehs()
obj3.move()