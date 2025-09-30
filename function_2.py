""" 
function categories :::::::::::

there are 4 types of function :=
1) function without parameters and function without return type.
2) function with parameters and function without return type.
3) function without parameters and function with return type.
4) function with parameters and function with return type.
"""

# 2)------------------

# def addition(num1,num2):
#     ans=num1+num2
#     print(ans)
# n1=int(input("eneter the number : "))
# n2=int(input("eneter the number : "))
# addition(n1,n2)

# 3)---------------------

# def mul():
#     num1=int(input("enter number 1 : "))
#     num2=int(input("enter number 2 : "))
#     return num1 * num2
# print(mul())

# 4)----------------------
l1=[1,2,3,4,5,6,7,8,9,10,99,89,656,45,32,978,4548,898,11,12,13]

def countEven(l1):
    count=0
    for i in l1:
        if i%2==0:
            count+=1
    return count

def countOdd(l1):
    count=0
    for i in l1:
        if i%2!=0:
            count+=1
    return count
print(f"total even numbers are :: {countEven(l1)}  \n total odd numbers are :: {countOdd(l1)} ")