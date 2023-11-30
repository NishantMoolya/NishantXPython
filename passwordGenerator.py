import random
from shlex import join

alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

special_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

alpha = int(input('Enter the count of alphabet you want: '))
num = int(input('Enter the count of number you want: '))
special = int(input('Enter the count of special character you want: '))

password = []

for i in range(alpha):
    genAlpha = random.randint(0,len(alpha_list))
    password+=alpha_list[genAlpha]
for i in range(num):
    genNum = random.randint(0,len(num_list))
    password+=num_list[genNum]
for i in range(special):
    genSpecial = random.randint(0,len(special_list))
    password+=special_list[genSpecial]
finalpass = random.shuffle(password)
print(finalpass)
print(f"Your generated password is {finalpass}")