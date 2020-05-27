## Nobody can find you here. No one can see what goes on here except for me, and probably Psy
## The deeper you go, the harder it is to find someone.
## I probably sound like a psychopath,
## Burying someone down here,
## But it is quite comfortable, isn't it?

import turtle
import math

n = int(input('Enter the number of iterations (Must be > 1): '))

if n > 0:
    print("Fibonacci series for", n, "elements")


x = turtle.Turtle()
def fiboPlot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b


    turtle.pencolor("Blue")


    turtle.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)


    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)


        temp = square_b
        square_b = square_b + square_a
        square_a = temp


    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()


    x.pencolor("red")


    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b


factor = 1



