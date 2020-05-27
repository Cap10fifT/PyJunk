import turtle
from turtle import Turtle, Screen
MIN_COLOR = 5
MAX_COLOR = 255
COUNT = 1080

def turtrun():
    t.width(r/100 + 1)
    t.forward(r)
    t.left(59)
    t.speed('fastest')


screen = Screen()
screen.colormode(255)

t = Turtle()
turtle.bgcolor('black')
for r in range(COUNT):

    red = round(r * ((MAX_COLOR - MIN_COLOR) / (COUNT - 1))) + MIN_COLOR

    color = (red, 0, 0)

    t.pencolor(color)
    turtrun()

screen.exitonclick()
turtle.done()
