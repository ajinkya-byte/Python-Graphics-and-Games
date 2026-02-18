import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.width(3)

# Face (Blue circle)
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.color("blue")
pen.begin_fill()
pen.circle(120)
pen.end_fill()

# Face inner (white)
pen.penup()
pen.goto(0, -70)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(90)
pen.end_fill()

# Left Eye
pen.penup()
pen.goto(-35, 50)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(25)
pen.end_fill()

# Right Eye
pen.penup()
pen.goto(35, 50)
pen.pendown()
pen.begin_fill()
pen.circle(25)
pen.end_fill()

# Left Pupil
pen.penup()
pen.goto(-25, 65)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(10)
pen.end_fill()

# Right Pupil
pen.penup()
pen.goto(45, 65)
pen.pendown()
pen.begin_fill()
pen.circle(10)
pen.end_fill()

# Nose
pen.penup()
pen.goto(0, 30)
pen.pendown()
pen.color("red")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# Mouth
pen.penup()
pen.goto(-40, 0)
pen.setheading(-60)
pen.pendown()
pen.circle(80, 120)

pen.hideturtle()
turtle.done()

