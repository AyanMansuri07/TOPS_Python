l1=["python","java","html"]
l2=[]
def convert(lst):
    global l2
    for i in lst:
        l2.append(i.upper())
convert(l1)
print(l2)

# with lampda map

l2 = list(map(lambda sub : sub.upper(),l1))
print(l2)