import turtle


def rectangle(leng, wid=0):
    if wid == 0:
        wid = leng

    i = 0
    while i < 2:
        turtle.forward(leng)
        turtle.right(90)
        turtle.forward(wid)
        turtle.right(90)
        i += 1


rectangle(200)
turtle.up()
turtle.forward(25)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.down()
rectangle(150, 50)
turtle.up()
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.down()
rectangle(50, 150)
turtle.exitonclick()