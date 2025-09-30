# withou filter 
l1 = [12,34,67,9,56,34]
l2=[]
def myfun(list):
    global l2
    for i in list:
        if i%2==0:
            l2.append(i)
myfun(l1)
print(l2)

# with filter 

l1=[12,4,7,98,3]
l2=list(filter(lambda num : num%2==0,l1))
print(l2)

# with map

l3=list(map(lambda num : num%2==0,l1))
print(l3)