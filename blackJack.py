import random

card_list = ['a','2','3','4','5','6','7','8','9','k','j','q','k']
value_list = [1,2,3,4,5,6,7,8,9,10,10,10,10]
user_list = []
cpu_list = []
for i in range(2):
    card = random.choice(card_list)
    cpucard = random.choice(card_list)
    user_list.append(card)
    cpu_list.append(cpucard)
print(user_list)
print(cpu_list)