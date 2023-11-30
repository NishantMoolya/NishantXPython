alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
len(alphabets)
word = input("Enter the message: ")
key = int(input("Enter crypting key: "))
encrypt = ""
for i in word:
    for a in range(25):
        if i == alphabets[a]:
            if a+key > 25:
                encrypt+=alphabets[(a+key)-25]
            else:
                encrypt+=alphabets[a+key]
print(f"Encrypted : {encrypt}")