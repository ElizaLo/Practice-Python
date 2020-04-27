import turtle
import math
wn = turtle.Screen()
wn.bgcolor("SkyBlue")
bob = turtle.Turtle()
bob.right(90)
for _ in range(4):
    bob.forward(50)
    bob.left(90)
bob.right(225)
distance = math.sqrt(50*50 / 2)
bob.forward(distance)
bob.right(90)
bob.forward(distance)
wn.exitonclick()

