# 1
# 00
# 111
# 0000

row =5
for row in range(6):
    for col in range(1,row+1):
            print(row%2,end="")
    print()
    
row =5
for row in range(6):
    for col in range(1,row+1):
            if row%2==0:
                print("0",end=" ")
            else:
                print("1",end=" ")
    print()
    