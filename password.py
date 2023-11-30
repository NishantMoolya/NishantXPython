
from ast import List
import random
import string

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ';', ':', '\'', '"', '<', '>', ',', '.', '?', '/']

combo = [capital_letters,small_letters,numbers,special_characters]
passLen = int(input("Enter the length: "))
password = ""
newList = []
password+=random.choice(capital_letters)
password+=random.choice(small_letters)
password+=random.choice(numbers)
password+=random.choice(special_characters)
for i in range(0,passLen-4):
    newList = random.choice(combo)
    password+=random.choice(newList)

newList = list(password)
random.shuffle(newList)
print(f"Your generated password is: {"".join(newList)}")
             