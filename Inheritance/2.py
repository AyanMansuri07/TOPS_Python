class A:
    def displayA(self):
        print(" this A class")
class B(A):
    def displayB(self):
        print("this is B class")
class C(B):
    def displayC(self):
        print("this is C class")
        

obj1=C()

obj1.displayA()
obj1.displayB()
obj1.displayC()