# --------------------------------------
# CSCI 127, Lab 2
# September 12, 2017
# Austin Hull
# --------------------------------------

import turtle
import random

border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.up()
border.goto(-300, 300)
border.down()
for side in range(4):
    border.forward(600)
    border.right(90)

lollipop = turtle.Turtle()
lollipop.color("red")
lollipop.hideturtle()
lollipop.speed(0)

stick = turtle.Turtle()
stick.color("black")
stick.width(5)
stick.hideturtle()
stick.speed(0)
stick.right(90)

""" 
Do not delete or change any of the Python statements above this line.

The next 4 statements illustrate a lollipop of radius 30 whose bottom 
is at (0,0) and a stick of length 60 whose top appears at (0, 0)
"""


def draw_lollipop(width, spot1, spot2):
    lollipop.up()
    lollipop.goto(spot1, spot2)
    lollipop.down()
    lollipop.begin_fill()
    lollipop.circle(width)
    lollipop.end_fill()
    stick.up()
    stick.goto(spot1, spot2)
    stick.down()
    stick.forward(2 * width)
    

for i in range(100):
    a = random.randrange(10, 30)
    x = random.randrange(-300 + a, 300 - a)
    y = random.randrange(-300 + (2*a), 300 - (2*a))
    draw_lollipop(a, x, y)

