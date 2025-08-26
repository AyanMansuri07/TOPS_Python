counteven =0
countodd =0
for i in range(1,6):
    num = int(input("enter number "))
    if num %2 ==0:
        counteven = counteven+1
    else:
        countodd = countodd+1

print("count of even number is ",counteven)
print("count of odd number is ",countodd)
