# Practical Example 6: Write a Python program to check if a number is prime using if_else.
num=int(input("Enter number: "))
flag =0
for i in range(2,num):
    if num % i==0:
        flag =1
    
if flag==0:
    print("prime number")
else:
    print("not prime number")