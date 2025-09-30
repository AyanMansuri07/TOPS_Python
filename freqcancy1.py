l1=["python","java","python","fulter","react","java"]
d={}

for i in l1:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
print(d)