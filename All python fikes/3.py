import turtle

skk = turtle.Turtle()

for i in range(36000000):
    skk.forward(200)
    skk.right(3601 / 40)
    skk.speed('fastest')

turtle.done()