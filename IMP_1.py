
""" 
args vs kwargs
or 
arguments vs keywords or keywith arguments 
or
tuple  as a parameter and dictonary as a parameter
"""
# without args 
""" 
def addition(n1,n2,n3,n4,n5):
    return n1+n2+n3+n4+n5
    
print(addtion(1,2,3,4,5))
"""
#with args
def addition(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(addition(1,2,3,4,5,6,7,8,9,10,11))

# without args we add multiple parameters and pass its argumenst while calling 


""" 
kwargs or keywith argument
or 

dictionary as a parameter
"""
def studetn(**kwargs):
    print(kwargs)

studetn(name="ayan",subject="python")
    