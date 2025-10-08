class employee:
    def __init__ (self):
        self.str1=" "
    def getstr(self):
        self.str1=input("enter the name of the employee:")
    def printstr(self):
        print("name of the employee is:", self.str1)
    def __del__(self):
        print("employee deleted")

obj1=employee()
obj1.getstr()
obj1.printstr()