import random
num  = int(input('Enter the number question paper required: '))
que_list = ['added to','substracted from','multiplied to','divided by']
score = 0
for i in range(num):
    a = random.randint(0,10)
    b = random.randint(0,10)
    qnum = random.randint(0,3)      
    print(f"{i+1}) {a} is {que_list[qnum]} {b}")
    ans = float(input("Enter your answer: "))
    if qnum == 0:
        if ans == (a+b): 
            score+=1
    elif qnum == 1:
        if ans == (a-b):
            score+=1
    elif qnum == 2:
        if ans == (a*b):
            score+=1
    elif qnum == 3:
        if ans == (a/b):
            score+=1
    print(f"Your score is {score}")

