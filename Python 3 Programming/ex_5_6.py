import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle") # arrow, blank, circle, classic, square, triangle, turtle

dist = 5
tess.up()                     # this is new
for _ in range(30):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 2
wn.exitonclick()

