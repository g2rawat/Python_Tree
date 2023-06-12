from random import randint
from turtle import Turtle, Screen, turtles
import turtle
screen=Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.colormode(255)
screen.title("Tree")
oak=turtle.Turtle()
oak.pencolor("black")
oak.width(10)
oak.speed("fast")
oak.up()
oak.left(90)
oak.bk(200)
oak.down()
angle=30
def tree(l):
    if l<10:
        return
    else:
        oak.color(randint(0,255),randint(0,255),randint(0,255))
        screen.update()
        oak.forward(l)
        oak.right(angle)
        tree(3*l/4)
        oak.left(angle*2)
        tree(3*l/4)
        oak.right(angle)
        oak.bk(l)

tree(100)

screen.exitonclick()
