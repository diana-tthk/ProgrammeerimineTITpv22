from turtle import *

def drawSquare():
    i = 0
    while i < 4:
        forward(30)
        left(90)
        i += 1

y = 0
while y < 3: 
    drawSquare()
    up()
    forward(100)
    left(90)
    forward(100)
    down()
    y += 1

exitonclick()
