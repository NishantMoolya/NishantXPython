import random
actions = ["rock","paper","scissor"]

gameOn = 10
userScore = 0
cpuScore = 0
print("Get Ready with your numeric pad\n")
while(gameOn):
    cpuMove = random.choice(actions)
    num = int(input("Enter your move(1 - rock,2 - paper,3 - scissor): "))
    userMove = actions[num-1]
    if userMove != cpuMove:
        if userMove == actions[0]:
            if cpuMove == actions[1]:
                print("Try again")
                cpuScore+=1
            else:
                print("Good move")
                userScore+=1
        if userMove == actions[1]:
            if cpuMove == actions[2]:
                print("Try again")
                cpuScore+=1
            else:
                print("Good move")
                userScore+=1
        if userMove == actions[2]:
            if cpuMove == actions[0]:
                print("Try again")
                cpuScore+=1
            else:
                print("Good move")
                userScore+=1
    else:
        print("Same choice")
    gameOn-=1

print(f"Your Score is {userScore}   Cpu Score is {cpuScore}")
if userScore > cpuScore :
    print("You won the game")
elif userScore == cpuScore:
    print("Its a tie!")
else:
    print("Cpu won try next time!")