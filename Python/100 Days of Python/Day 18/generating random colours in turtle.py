# drawing a random walk using random colours and directions

from turtle import Turtle, Screen
import random

# Set up the screen for the drawing and set the color mode to 255.
# This must be done before the turtle starts drawing with RGB colors.
screen = Screen()
screen.colormode(255)

# Create a new turtle object
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

# Use random rgb colours
def random_color():
    """Generates a random RGB color tuple."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

for _ in range(200):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.setheading(random.choice(directions))
    timmy_the_turtle.forward(30)

# The screen.exitonclick() line keeps the window open
# until you click on it, so you can see the result.
screen.exitonclick()
