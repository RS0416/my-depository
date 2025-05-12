n=int(input("the n value i:"))
no=1
for i in range(n):
    for j in range(i+1):
        print(no,end=" ")
        no=no+1
    print( )