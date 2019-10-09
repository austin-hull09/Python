import turtle
import random

window = turtle.Screen()

square = turtle.Turtle()
square.speed(0)
square.hideturtle()

square.up()
square.goto(-200, 200)
square.down()


for i in range(4):
    square.forward(50)
    square.right(90)

square.up()
square.goto(-205, 205)
square.write("Change Color")

pencil = turtle.Turtle()
pencil.shape("circle")

def drawing_controls(x, y):
    if (-200 <= x <= -150) and (150 <= y <= 200):
        a=random.random()
        b=random.random()
        c=random.random()
        pencil.color(a,b,c)
        square.color(a,b,c)
        square.goto(-200,200)
        square.down()
        for i in range(4):
            square.forward(50)
            square.right(90)
    

    
window.onclick(drawing_controls)


pencil.onrelease(pencil.goto)




