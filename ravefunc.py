def revno(no):
    c=0
    while no>0:
        digit=no%10
        c=c+1
        no=no//10
    return c
num=int(input("enter a no.:"))
print("no. of digits",revno(num))