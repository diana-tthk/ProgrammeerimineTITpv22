from turtle import *


def draw_square(length):
    i = 0
    forward(length/2)
    while i < 3:
        right(90)
        forward(length)
        i += 1
    right(90)
    forward(length/2)


i = 0
while i < 5:
    draw_square(100)
    right(72)
    i += 1

exitonclick()
