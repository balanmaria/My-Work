from turtle import Turtle, Screen
import random

tim=Turtle()

# #draw a triangle
# tim.color("blue")
# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)
#
# #draw a square
# tim.color("grey")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# #draw a pentagon
# tim.color("red")
# for _ in range(5):
#     tim.forward(100)
#     tim.right(72)
#
# #draw a hexagon
# for _ in range(6):
#     tim.forward(100)
#     tim.right(60)
#
# #draw a heptagon
# for _ in range(7):
#     tim.forward(100)
#     tim.right(51.5)
#
# #draw a octagon
# for _ in range(8):
#     tim.forward(100)
#     tim.right(45)
#
# #draw a nonagon
# for _ in range(9):
#     tim.forward(100)
#     tim.right(40)
#
# #draw a decagon
# for _ in range(10):
#     tim.forward(100)
#     tim.right(36)

colors=["blue", "cyan", "green", "black", "magenta", "red", "yellow"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

screen=Screen()
screen.exitonclick()