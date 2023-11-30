from turtle import Screen, Turtle

tim = Turtle() 
screen = Screen()
tim.shape("turtle")
tim.color("red")
tim.forward(100)
tim.begin_fill()
tim.circle(100)
tim.end_fill()


screen.exitonclick()