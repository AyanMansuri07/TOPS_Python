# take three number and check wich one is gretest

n1 = int(input("enter the first number "))
n2 = int(input("enter the second number "))
n3 = int(input("enter the third number "))

if n1>n2:
    if n1>n3:
        print(n1,"is greter")
    else:
        print(n3,"is greter")
else:
    if n2>n3:
        print(n2,"is greter")
    else:
        print(n3,"is greter ")


# if n1>n2 and n1>n3:
#     print(n1,"is greter")
# elif n2>n1 and n2>n3:
#     print(n2,"is greter ")
# else:
#     print(n3,"is greter ")
    