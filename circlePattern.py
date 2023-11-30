from turtle import Screen, Turtle
import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.speed(0)
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'Black', 'White', 'Brown']

for i in range(180):
    num = random.randint(0,9)
    tim.color(colors[num])
    tim.circle(100)
    tim.left(2)

screen.exitonclick()