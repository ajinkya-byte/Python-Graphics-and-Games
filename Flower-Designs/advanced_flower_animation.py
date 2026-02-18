import turtle

screen = turtle.Screen()
screen.bgcolor("black")

flower = turtle.Turtle()
flower.speed(0)
flower.width(2)

colors = ["red", "yellow", "pink", "orange", "purple", "cyan"]

for i in range(60):
    flower.color(colors[i % 6])
    flower.circle(100)
    flower.left(6)

flower.hideturtle()
turtle.done()

