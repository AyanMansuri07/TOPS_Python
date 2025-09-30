l1=["python","java","android","php","react"]

# with map
l2=list(map(lambda sub : len(sub),l1))
print(l2)

l2=list(map(lambda sub : len(sub)>4,l1))
print(l2)

# with filter 
l2 = list(filter(lambda sub : len(sub)>4,l1))
print(l2)
