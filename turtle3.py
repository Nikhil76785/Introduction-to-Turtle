import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300, 400)

t = turtle.Turtle()
size = 0

while True:
    for i in range(4):
        t.fd(size + 1)
        t.left(90)
        size = size - 5

    size = size + 1