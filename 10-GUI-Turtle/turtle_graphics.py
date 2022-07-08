import random
import turtle as t

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

turtle = t.Turtle()
turtle.shape("turtle")
turtle.color("red")


def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)


def draw_dashed_line():
    for _ in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.left(angle)


def draw_shape_art():
    for side in range(3, 11):
        turtle.color(random.choice(colors))
        draw_shape(side)


screen = t.Screen()
screen.exitonclick()
