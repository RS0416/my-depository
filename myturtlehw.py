import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300, 400)
polygon=turtle.Turtle()
sides=int(input("enter the no. of sides:"))
l=10
angle=180/sides
for i in range(sides):
    polygon.forward(l)
    polygon.right(angle)
turtle.done()