def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact *= i
    return fact

def isPostive(num):
    if num>0:
        return "Positive"
    else:
        return "Nagative"
    
print(factorial(5))