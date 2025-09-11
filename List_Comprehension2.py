# with list comprehansion 
l1=[1,2,3,4,56,6,7,8,9,10,11,21]
#    [element     loop             condition ]  
#     3     1         2  
#    -- ---------  ---------
l2 =[i for i in l1 if i%2==0]
print(l2)

#withou 

l3=[]
for i in l1:
    if i%2==0:
        l3.append(i)
print(l3)