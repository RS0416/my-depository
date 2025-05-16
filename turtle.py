import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300, 400)
polygon=turtle.Turtle()
input("no. of sides", 6)
sides=input("enter the no. of sides:")
l=100
angle=360/sides
for i in range(sides):
    polygon.forward(l)
    polygon.right(angle)
turtle.done()