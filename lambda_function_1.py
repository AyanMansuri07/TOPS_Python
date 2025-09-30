# withour lambda 
def addition(num1,num2):
    return num1+num2

num1 = int(input("enter the number : "))
num2 = int(input("enter the number : "))

print(addition(num1,num2))

# with lambda
ans = lambda a,b : a+b
print("lambda function ",ans(num1,num2))