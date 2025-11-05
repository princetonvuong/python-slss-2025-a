# Loops
# Author:Princeton Vuong
# October 14

import random
import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("violet")

# TMNT - turtles
mikey = turtle.Turtle()
# mikey.turtlesize()  # size
mikey.color("orange")
mikey.width(5)
mikey.pencolor("white")
mikey.shape("circle")
mikey.hideturtle()
# m.circle(100)
# m.penup()
# m.goto(0, -400)
# m.pendown()
# m.circle(200)
# m.penup()
# m.goto(0, 200)
# m.pendown()
# m.circle(50)
#
# MAKE 100 COOKIES
for counter in range(10):
    counter = counter * 50
    # Make sure that turtle is pointing east
    mikey.setheading(0)
    # change the cookie colour
    mikey.color("brown")
    # draw a circle
    mikey.pu()
    mikey.goto(-5 + counter, -30 + counter)
    mikey.pd()
    mikey.circle(30)

    # put a chocolate chip on the top left side
    mikey.pu()
    mikey.goto(-10 + counter, 10 + counter)
    mikey.stamp()

    # chocolate chip on the top right
    mikey.goto(10 + counter, 10 + counter)
    mikey.stamp()

    # choco chip on the bottom right
    mikey.goto(10 + counter, -10 + counter)
    mikey.stamp()

    # ch chip on the bottom left
    mikey.goto(-10 + counter, -10 + counter)
    mikey.stamp()

    # ch chip in the middle
    mikey.goto(0 + counter, 0 + counter)
    mikey.stamp()

# make cookies in random lcotions
# make 1000 cookies


for _ in range(1000):
    x = random.randrange(-700, 700)
    y = random.randrange(-700, 700)


window.exitonclick()
