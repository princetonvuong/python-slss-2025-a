# Make a drawing
# Author: Princeton Vuong
# October 28
#
import turtle
import random

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
wn = turtle.Screen()
wn.bgcolor("white")


BMW_BLUE = "#0066B1"
WHITE = "#FFFFFF"
BLACK = "#000000"
GRAY = "#C0C0C0"


def draw_filled_circle(radius, color):
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()
    t.home()


outer_radius = 200
white_ring_inner = 170
black_inner_radius = 200
quadrant_radius = 140
gray_inner = 145
gray_outer = 210

draw_filled_circle(gray_outer, GRAY)
draw_filled_circle(outer_radius, BLACK)
draw_filled_circle(white_ring_inner, WHITE)
draw_filled_circle(black_inner_radius, BLACK)
draw_filled_circle(gray_inner, GRAY)


def draw_quadrant(color, start_angle):
    t.penup()
    t.goto(0, 0)
    t.setheading(start_angle)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.forward(quadrant_radius)
    t.left(90)
    t.circle(quadrant_radius, 90)
    t.goto(0, 0)
    t.end_fill()
    t.penup()
    t.home()


# Draw BMW quadrants
draw_quadrant(BMW_BLUE, 90)  # Top-left
draw_quadrant(WHITE, 0)  # Top-right
draw_quadrant(BMW_BLUE, 270)  # Bottom-right
draw_quadrant(WHITE, 180)  # Bottom-left


t.penup()
t.goto(0, -quadrant_radius)
t.setheading(0)
t.pendown()
t.width(5)
t.color(BLACK)
t.circle(quadrant_radius)
t.penup()
t.home()

t.color(WHITE)
t.goto(-60, 130)
t.write("B", align="center", font=("Arial", 48, "bold"))
t.goto(0, 140)
t.write("M", align="center", font=("Arial", 48, "bold"))
t.goto(60, 130)
t.write("W", align="center", font=("Arial", 48, "bold"))

t.penup()

colors = ["black", "#11FFEE", "#FF1199"]

num_stars = 300
star_area = 700

for _ in range(num_stars):
    # Random x, y position
    x = random.randint(-star_area, star_area)
    y = random.randint(-star_area, star_area)

    # Random size for variety
    size = random.randint(2, 5)

    t.goto(x, y)
    t.dot(size, random.choice(colors))


wn.exitonclick()
