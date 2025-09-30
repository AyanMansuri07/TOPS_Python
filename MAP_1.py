"""
map() : map is an inbuld function in python whichi is iterate each 
elements and return in map format.
syntazx : 
    = map(function,iterator)
"""
l1=[1,2,3,4,5,6,7,8,9,10]

# ::without 

l2=[]
def increment(lst):
    global l2
    for i in lst:
        l2.append(i+5)
increment(l1)
print("without : ",l2)

# :: with map

def increment(lst):
    return lst + 5

l2 = list(map(increment,l1))
print("with : ",l2)

# :: with map and lambda

l2=list(map(lambda num : num+5,l1))
print("lambda , map : ",l2)

l2 =[i+5 for i in l1]
print("list comprehansion : ",l2)
