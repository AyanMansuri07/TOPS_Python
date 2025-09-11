num = 5
flag = True
for i in range(2,num):
    if (num %i==0):
        flag = False
        break

if flag:
    print("yes")
else:
    print("not")