try : 
    n1 = int(input("enter the nubmer : "))
    n2 = int(input("enter the nubmer : "))
    
    ans = n1/n2
except ValueError:
    print("invalid error ")
except ZeroDivisionError:
    print("number can not divide by zero ")
else:
    print(ans)
finally:
    print("thank you for using this app 😂😂😂😂😂😂😂😂😂😂😂")