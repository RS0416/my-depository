#sum of in natural
a=int(input("enter the value whose sum you want to find:"))
sum=0
for i in range(1, a+1):
    sum=sum+i
print(sum)
#print the numbers in reverse order
b=int(input("enter the value whose order you want to find:"))
for i in range(b,0,-1):
    print(i)
#print the string in reverse order
string2=input("enter the string:")
str2=("")
for i in string2:
    str2= i+str2
print("the original string",string2)
print("the reversed string",str2)