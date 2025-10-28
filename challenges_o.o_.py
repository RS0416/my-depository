class a:
    def __init__ (self, a):
        self.a= a
    def __lt__ (self, other):
        if(self.a<other.a):
            return "ob1 is less than ob2."
        else:
            return "ob1 is greater than ob2. "
    def __eq__ (self, other):
        if(self.a == other.a):
            return "Both no. are equal."
        else:
            return "Both no. are not equal."

ob1= a(2)
ob2= a(3)
print("Print passed values:", ob1.a, ob2.a)
print(ob1 < ob2)
ob3= a(4)
ob4= a(5)
print("Print passed values", ob3.a, ob4.a)
print(ob3 == ob4)