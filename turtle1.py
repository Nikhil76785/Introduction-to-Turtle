import turtle

turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(300, 400)

t = turtle.Turtle()
num_sides = 6
side_length = 70
angle = 360 / num_sides

for i in range(num_sides):
    t.forward(side_length)
    t.right(angle)

