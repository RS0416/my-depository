try:
    age1=eval(input("enter the age."))
    res=age1/2
    print("the result is",res)
except ZeroDivisionError:
    print("there is an error in division by zero.")
except ValueError:
    print("the input is wrong.")
finally:
    print("This will execute no matter what.")