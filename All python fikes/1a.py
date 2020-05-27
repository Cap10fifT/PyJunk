import turtle, math


colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

myWin = turtle.Screen()
t = turtle.Pen()
x = 1

turtle.bgcolor('black')

s = 2
a = 2

t.up()
t.left(90)
t.backward(s / 2)
t.down()

for x in range(361):
    t.pencolor(colors[x % 6])
    t.speed(500)
    t.forward(s)
    t.left(a)


myWin.exitonclick()
turtle.done()