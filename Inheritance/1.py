""" 
Single Inheritance 
"""
class A:
    def displayA(self):
        print("this is A class")
class B(A):
    def displayB(self):
        print("this is B class")

obj  = B()

obj.displayA()
obj.displayB()