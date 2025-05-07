a=int(input("enter the value:"))
sum=0
temp=a
while temp>0:
    rem=temp%10
    print(rem)
    sum+=1
    temp//=10
print("no. of digits ",sum)