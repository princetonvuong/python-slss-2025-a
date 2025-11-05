# Recursion
# Author: PRinceton VUong
# 20 October
#
# Were drawing trees (recursively)

import turtle

# # Create a turtle that draws
t = turtle.Turtle()

window = turtle.Screen()
window.bgcolor("white")


# def draw_tree(level: int, branch_length: float):
#     """A recursive function to draw trees
#     level - the levels of branches
#     branch_length - length of branch to draw
#     """
#     # Base case is when level is 0
#     if level == 0:
#         # Create a leaf
#         t.color("darkgreen")
#         t.stamp()
#         t.color("brown")
#     # For all other levels
#     else:
#         # # 1. Go forwards branch_length pixels
#         # t.forward(branch_length)
#         # # 2. turn to the left and draw a -1 level tree
#         # t.left(37)
#         # draw_tree(level - 1, branch_length * 0.8)
#         # # 3. turn right and draw a -1 level tree
#         # t.right(74)
#         # draw_tree(level - 1, branch_length * 0.8)
#         # # 4. Go back to where we started
#         # t.left(37)
#         # t.backward(branch_length)


# # Set up turtle

# # t.left(90)
# # t.color("brown")
# # t.pensize(5)
# # t.shape("turtle")
# # t.penup()
# # t.goto(0, -180)
# # t.pendown()

# # draw_tree(1, 128)

# Dictionary to hold colours
LEAF_COLOURS = {
    "spring": "#ffb5c2",
    "summer": "#a9fbc3",
    "fall": "#99621e",
    "winter": "f#7f7f2",
}


def draw_complicated_tree(level: int, branch_length: float):
    """Draw a recursive tree with more than 2 branches per level."""
    if level == 0:
        # Draw a leaf
        t.color(LEAF_COLOURS["spring"])
        t.stamp()
        t.color("brown")
    else:
        t.forward(branch_length)
        # First branch (left)
        t.left(30)
        draw_complicated_tree(level - 1, branch_length * 0.7)
        # Second branch (middle)
        t.right(30)  # back to center
        draw_complicated_tree(level - 1, branch_length * 0.7)
        # Third branch (right)
        t.right(30)
        draw_complicated_tree(level - 1, branch_length * 0.7)
        # Return to center orientation
        t.left(30)
        # Go back to where we started
        t.backward(branch_length)


# --- Setup turtle screen ---
t.color("brown")
t.speed("fastest")
t.shape("turtle")
t.left(90)  # point upward
t.penup()
t.goto(0, -250)
t.pendown()

# --- Draw the tree ---
draw_complicated_tree(level=6, branch_length=80)

window.exitonclick()
