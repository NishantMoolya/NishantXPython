# star pattern-1
for i in range(1,5):
   print(f"{i*"*"}")

# 2 and 3 multiples
for i in range(2,4):
    for j in range(1,11):
        #print(f"{i} X {j} = {i*j}")
        print(f"{i} X {j} = {eval("i*j")}")
    print("\n\n")