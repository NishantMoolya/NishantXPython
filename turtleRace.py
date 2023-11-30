import random
from turtle import Turtle,Screen

screen = Screen()
screen.title("Turtle Race")
screen.bgcolor("black")

colors = ['blue', 'green', 'yellow', 'purple','red']
turtle_list = []
y_coord = [160,80,0,-80,-160]

for i in range(5):
    tur = Turtle()
    tur.shape("turtle")
    tur.color(colors[i])
    tur.penup()
    tur.goto(-300,y_coord[i])
    turtle_list.append(tur)
    
turtle_list[2].goto(300,-300)
turtle_list[2].pendown()
turtle_list[2].goto(300,300)
turtle_list[2].penup()
turtle_list[2].goto(-300,0)

announcer = Turtle()
announcer.color("white")
announcer.hideturtle()
user_bet = screen.textinput(title="Turtle Race",prompt="Which turtle will win the race?").lower()

game_on = True
while game_on:
    for i in turtle_list:
        num = random.randint(5,30)
        i.forward(num)
        if i.xcor() > 300:
            game_on = False
            if i.pencolor() == user_bet:
                announcer.write("You won the game!",align="center",font=("Aria",25,"bold"))
            else:
                announcer.write("You lost the game!",align="center",font=("Aria",25,"bold"))
screen.exitonclick()                                