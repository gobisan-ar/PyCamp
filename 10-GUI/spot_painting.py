import random
import colorgram
import turtle

def generate_color_palette(image_name):
    colors = colorgram.extract(image_name, 30)
    rgb_colors = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        gray_scale = 0.2126 * r + 0.7152 * g + 0.0722 * b

        if gray_scale < 240:
            new_color = (r, g, b)
            rgb_colors.append(new_color)

    return rgb_colors


color_palette = generate_color_palette('image.jpg')

turtle.colormode(255)

brush = turtle.Turtle()

brush.penup()
brush.hideturtle()
brush.speed("fastest")

brush.setheading(225)
brush.forward(300)
brush.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    brush.dot(20, random.choice(color_palette))
    brush.forward(50)

    if dot_count % 10 == 0:
        brush.setheading(90)
        brush.forward(50)
        brush.setheading(180)
        brush.forward(500)
        brush.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
