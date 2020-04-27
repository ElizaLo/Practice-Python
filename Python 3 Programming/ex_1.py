import turtle

bg_color  = input('Input background color:')
color = input('Input pen color:')
pen_size = int(input('Input pen size:'))

wn = turtle.Screen()
wn.bgcolor(bg_color)        # set the window background color

tess = turtle.Turtle()
tess.color(color)              # make tess blue
tess.pensize(pen_size)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas

