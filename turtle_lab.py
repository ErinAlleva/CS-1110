#Alex Hicks (awh4kc)

import turtle

virginia = turtle.Turtle()
virginia.speed("fastest")

virginia.penup()
virginia.goto(0,-200)
virginia.pendown()
virginia.color("darkorange")
virginia.begin_fill()
virginia.circle(200)
virginia.end_fill()

virginia.penup()
virginia.goto(-250,75)
virginia.pendown()
virginia.color("darkorange")
virginia.begin_fill()
virginia.goto(-250,-300)
virginia.goto(250,-300)
virginia.goto(250,75)
virginia.goto(-250,75)
virginia.end_fill()

virginia.penup()
virginia.goto(-250,80)
virginia.pendown()
virginia.color("white")
virginia.begin_fill()
virginia.goto(-250,70)
virginia.goto(250,70)
virginia.goto(250,80)
virginia.goto(-250,80)
virginia.end_fill()

virginia.penup()
virginia.goto(-250,-250)
virginia.pendown()
virginia.color("white")
virginia.begin_fill()
virginia.goto(-250,-260)
virginia.goto(250,-260)
virginia.goto(250,-250)
virginia.goto(-250,-250)
virginia.end_fill()

virginia.penup()
virginia.goto(-250,20)
virginia.pendown()
virginia.color("white")
virginia.begin_fill()
virginia.goto(-250,20)
virginia.goto(-250,10)
virginia.goto(250,10)
virginia.goto(250,20)
virginia.goto(-250,20)
virginia.end_fill()

virginia.penup()
virginia.goto(-150,20)
virginia.pendown()
virginia.color("white")
virginia.begin_fill()
virginia.goto(-150,-300)
virginia.goto(-140,-300)
virginia.goto(-140,20)
virginia.end_fill()

virginia.penup()
virginia.goto(150,20)
virginia.pendown()
virginia.color("white")
virginia.begin_fill()
virginia.goto(150,-300)
virginia.goto(140,-300)
virginia.goto(140,20)
virginia.end_fill()

virginia.penup()
virginia.goto(-90,20)
virginia.pendown()
virginia.color("white")
virginia.begin_fill()
virginia.goto(-90,-250)
virginia.goto(-80,-250)
virginia.goto(-80,20)
virginia.end_fill()

virginia.penup()
virginia.goto(90,20)
virginia.pendown()
virginia.color("white")
virginia.begin_fill()
virginia.goto(90,-250)
virginia.goto(80,-250)
virginia.goto(80,20)
virginia.end_fill()

virginia.penup()
virginia.goto(-30,20)
virginia.pendown()
virginia.color("white")
virginia.begin_fill()
virginia.goto(-30,-250)
virginia.goto(-20,-250)
virginia.goto(-20,20)
virginia.end_fill()

virginia.penup()
virginia.goto(30,20)
virginia.pendown()
virginia.color("white")
virginia.begin_fill()
virginia.goto(30,-250)
virginia.goto(20,-250)
virginia.goto(20,20)
virginia.end_fill()

virginia.penup()
virginia.goto(-25,75)
virginia.pendown()
virginia.color("white")
virginia.begin_fill()
virginia.goto(-150,20)
virginia.goto(-125,20)
virginia.goto(0,75)
virginia.goto(-25,75)
virginia.end_fill()

virginia.penup()
virginia.goto(25,75)
virginia.pendown()
virginia.color("white")
virginia.begin_fill()
virginia.goto(150,20)
virginia.goto(125,20)
virginia.goto(0,75)
virginia.goto(25,75)
virginia.end_fill()
virginia.penup()
virginia.goto(0,-290)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")

virginia.penup()
virginia.goto(240,0)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")
virginia.penup()
virginia.goto(-240,0)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")
virginia.penup()
virginia.goto(130,-270)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")
virginia.penup()
virginia.goto(-130,-270)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")
virginia.penup()
virginia.goto(160,-235)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")
virginia.penup()
virginia.goto(-160,-235)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")
virginia.penup()
virginia.goto(70,-280)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")
draw_star(4, "white")
virginia.penup()
virginia.goto(-70,-280)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")
draw_star(4, "white")
draw_star(4, "white")
virginia.penup()
virginia.goto(220,-58.75)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")
draw_star(4, "white")
draw_star(4, "white")
virginia.penup()
virginia.goto(-220,-58.75)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")
draw_star(4, "white")
draw_star(4, "white")
virginia.penup()
virginia.goto(180,-176.25)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")
draw_star(4, "white")
draw_star(4, "white")
virginia.penup()
virginia.goto(-180,-176.25)
virginia.pendown()

def draw_star(size, color):
    angle = 120
    virginia.fillcolor(color)
    virginia.begin_fill()
    virginia.color("white")

    for side in range(5):
        virginia.forward(size)
        virginia.right(angle)
        virginia.forward(size)
        virginia.right(72-angle)

    virginia.end_fill()
    virginia.penup()
    return

draw_star(4, "white")

turtle.done()