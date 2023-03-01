from turtle import Turtle, Screen

import heroes

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
screen = Screen()
screen.exitonclick()

print(heroes.gen())