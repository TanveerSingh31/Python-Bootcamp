# MRO - Method Resolution Order 
# Used when single class inherits multiple classes

class Parent:
    def getName():
        print("Parent getName ")

class B(Parent):
    def getName():
        print("B getName ")

class C(Parent):
    def getName():
        print("C getName ")


class D(B, C):
    pass

class X(C, B):
    pass

D.getName()
X.getName()
