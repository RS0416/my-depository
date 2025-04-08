num=2
if num>0:
 print("the number",num," is positive")
nom=-2
if nom<0:
 print("the number",nom,"is negative")
actual_amount=int(input("enter the actual amount:"))
increased_amount=int(input("enter the increased amount:"))
if actual_amount<increased_amount:
 amount=increased_amount-actual_amount
 print("we have a profit of amount{}".format(amount))
else:
 print("no profit, only loss")

