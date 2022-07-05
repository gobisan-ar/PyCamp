import random
import turtle as t

t.colormode(255)

turtle = t.Turtle()
turtle.speed("fastest")


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # tuple
    random_color = (r, g, b)
    return random_color


def draw_spirograph(gap):
    for _ in range(360 // gap):
        turtle.color(generate_random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()