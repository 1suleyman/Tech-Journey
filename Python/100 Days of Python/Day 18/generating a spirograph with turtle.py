from turtle import Turtle, Screen
import random

# Set up the screen for the drawing and set the color mode to 255.
# This must be done before the turtle starts drawing with RGB colors.
screen = Screen()
screen.colormode(255)

# Create a new turtle object
tim = Turtle()
tim.shape("turtle")

# Use random rgb colours
def random_color():
    """Generates a random RGB color tuple."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")
# drawing a spiral with random colours
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)

# The screen.exitonclick() line keeps the window open
# until you click on it, so you can see the result.
screen.exitonclick()
