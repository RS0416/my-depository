a=input("enter the word:")
for i in a:
    if (i=="a"):
        print("the letter a is found")
        break
    else:
        print("the letter a is not found")

for i in range (10,20):
    if i%5==0:
        print("done") 
    elif i%3==0:
        print("TWIST")
    elif i%7==0:
        pass
    else:
        print(i)  