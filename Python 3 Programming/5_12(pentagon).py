import turtle

wn = turtle.Screen()
t = turtle.Turtle()

t.color('Blue')
t.shape('turtle')
t.speed(2)
t.left(18)
for _ in range(5):
    t.forward(100)
    t.left(72)

wn.exitonclick() 
