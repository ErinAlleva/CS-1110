# Alex Hicks (awh4kc)

import turtle

def draw_tree(t, depth):

    if depth == 0:
        return

    t.forward(30)
    t.left(30)
    t.forward(30)

    draw_tree(t,depth-1)

    t.back(30)
    t.right(60)
    t.forward(30)

    draw_tree(t, depth-1)

    t.back(30)
    t.left(30)
    t.back(30)

tom = turtle.Turtle()
tom.left(90)
tom.penup()
tom.back(150)
tom.speed("fastest")
tom.pendown()
draw_tree(tom, 5)

turtle.done()
