"""
We present another example of multiple inheritence, the diamond problem
"""

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")

class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    pass

x = D()
x.m()   #we get that m of B is called

#if we define       class D(C,B) and then perform the same;
# we get that m of C is called

class D(C,B):
    pass

x = D()
x.m()

###############################
print()
##############################

#let us consider that D also has its m method

class D(B,C):
    def m(self):
        print('m of D called')


x = D()
x.m()  #it does not calls all subclass m, as it has been overridden
print()
B.m(x)
C.m(x)
A.m(x)
print()

#so we can again redefine;
class D(B,C):
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)
        A.m(self)

x = D()
x.m()  #this is what we have been looking for

print()

#################################################
# similar to that, we redefine the whole class

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
        A.m(self)
    
class C(A):
    def m(self):
        print("m of C called")
        A.m(self)

class D(B,C):
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)

x = D()
x.m()  #a is called twice, which is not what we wanted
print()
#a pythonic way is to use super

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
        super().m()
    
class C(A):
    def m(self):
        print("m of C called")
        super().m()

class D(B,C):
    def m(self):
        print("m of D called")
        super().m()


#super() invokes the methods of the inheriting class, but only once

x = D()
x.m()



























