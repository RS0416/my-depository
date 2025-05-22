res=""
x=int(input("enter the value of x:"))
while x>0:
    eqat=x%2
    res=str(eqat)+res
    x=x//2
print(res)