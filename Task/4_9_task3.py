# accept 6 number from user and store positive in positive list and nagative
p_list=[]
n_list=[]

for i in range(6):
    add = int(input("enter the number : "))
    if add<0:
        n_list.append(add)
    else:
        p_list.append(add)
        
print("positive lils : ",p_list)
print("nagative list : ",n_list)