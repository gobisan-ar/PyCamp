import random
import turtle as t

directions = [0, 90, 180, 270]

t.colormode(255)

turtle = t.Turtle()
turtle.shape("turtle")
turtle.pensize(15)
turtle.speed("fastest")


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # tuple
    random_color = (r, g, b)
    return random_color


def random_walk():
    for _ in range(100):
        turtle.color(generate_random_color())
        turtle.setheading(random.choice(directions))
        turtle.forward(30)


random_walk()

screen = t.Screen()
screen.exitonclick()
