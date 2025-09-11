# accept 5 number from user and store even numbers in odd list
list1=[]
even=[]
odd =[]

for i in range(5):
    add = int(input("entter the elements : "))
    list1.append(add)

for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(list1)
print(even)
print(odd)