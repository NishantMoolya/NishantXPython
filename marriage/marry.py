with open("./marriage/names.txt","r") as file:
    content = file.read()
    #print(content)
    names_list = content.split("\n")
print(names_list)
for i in range(len(names_list)):
    with open(f"./marriage/invite{i+1}","w") as inviteFile:
        inviteText = "Dear "+names_list[i]+",\nPlease honor us with your presence as we exchange vows of love and commitment\nat Kinnigoli,Mangalore on 30th November at 12:35 PM.\nYour support is treasured as we embark on this beautiful journey together.\tYour presence would make our day complete."
        inviteFile.write(inviteText)