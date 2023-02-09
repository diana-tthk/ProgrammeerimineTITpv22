from turtle import *


def draw_square(length):
    i = 0
    while i < 4:
        forward(length)
        right(90)
        i += 1


i = 0
while i < 5:
    up()
    forward(36)
    down()
    draw_square(100)
    up()
    forward(36)
    down()
    right(72)
    i += 1

exitonclick()
