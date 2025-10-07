try:
    num1 = int(input("enter the number 1 : "))
    num2 = int(input("enter the number 2 : "))
    
    ans=num1/num2
    print(ans)
except ValueError:
    print("enter proper value")
except ZeroDivisionError:
    print("cannot be divide by zero")