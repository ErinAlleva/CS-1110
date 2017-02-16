# Alex Hicks (awh4kc)

import turtle
import random

yurtle = turtle.Turtle()
yurtle.speed("fastest")

colors = ["green", "red", "yellow", "cyan", "orange", "pink"]

def draw_shape(my_turtle, x, y, num_sides, size):
    my_turtle.penup()
    my_turtle.goto(x,y)
    my_turtle.pendown()
    rand_color = random.randint(0, len(colors) - 1)
    my_turtle.color(colors[rand_color])
    my_turtle.begin_fill()
    for i in range(num_sides):

        my_turtle.forward(size)
        my_turtle.left(360/num_sides)
    my_turtle.end_fill()

for i in range (20):
    rand_x = random.randint(-300,300)
    rand_y = random.randint(-300,300)
    rand_size = random.randint(10,100)
    rand_sides = random.randint(3,12)
    draw_shape(yurtle, rand_x, rand_y, rand_sides, rand_size)

draw_shape(yurtle, 50, -50)

turtle.done()
