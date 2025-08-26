a = int(input("enter first number :"))
b = int(input("Enter second number : "))

print("1.addition ")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulous")

ch= int(input("Enter your choice : "))
if ch==1:
    print("additon : ",a+b)
elif ch==2:
    print("subtraction : ",a-b)
elif ch==3:
    print("multiplication : ",a*b)
elif ch==4:
    print("division : ",a/b)
elif ch==5:
    print("modulous : ",a%b)
else:
    print("invalid choice !!!")