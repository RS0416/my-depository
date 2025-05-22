def power(x,y):
    p=1
    for i in range (1,3):
        p=p*x
    return p
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
print("the power of the number is ",power(x,y))