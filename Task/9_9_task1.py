# l1 = ["python","java"]
# l2 = [i.upper() for i in l1]
# print(l2)

# l1 =["java","python","android"]
# l2 =[len(i) for i in l1 if len(i)>4]
# print(l2)


# l1 = ["java","flutter","android","oops"]
# # --- method 1
# l2 = [i for i in l1 if i[0]=='a' or i[0]=='e' or i[0]=='o' or i[0] =='u']
# print(l2)
# # --- method 2
# l3=[i for i in l1 if i[0] in "aiou"]
# print(l3)

# l1 = ["java","flutter","android","oops"]
# l2 = [i[:3].upper() + i[3:].lower() for i in l1]
# print(l2) 

l1 =[1,2,5,6,6,7,8,9,9,5,1,0,10,12,11,21]
print(l1.count(6))
print(l1.index(12))