import turtle
from turtle import Turtle, Screen
from turtle import Turtle, Screen

mincolor = 5
maxcolor = 255
count = 10
screen = Screen()
tur = Turtle()

screen.colormode(255)

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(60)
        tree(branchLen-5,t)
        t.left(120)
        tree(branchLen-5,t)
        t.right(60)
        t.backward(branchLen)

for x in range(count):

    red = round(x * ((maxcolor - mincolor) / (count - 1))) + mincolor

    color = (red, 0, 0)

    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color(color)
    tree(200,t)
    myWin.exitonclick()
    t.speed('fastest')


