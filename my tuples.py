mytuple=("swastika",11,33.42,5.3)
print(mytuple)
mytuple1=("mumma",41,51.92,5.2)
print(mytuple1)
print(mytuple1[2:4])

newtuple=(1,2,3,4,5,4,3,2,1)
e=len(newtuple)-1
s=0
flag=0
while s<=e:
    if newtuple[e]!=newtuple[s]:
        print("not a palindrone.")
        flag=1
        break
    s+=1
    e-=1
if flag==0:
    print("its a palindrone.")