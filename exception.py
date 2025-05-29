try:
    num1, num2=eval(input("enter two no.:"))
    res=num1/num2
except ZeroDivisionError:
    print("division by zero is aa error.")
except SyntaxError:
    print("syntax error")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("this will execute no matter what.")