"""
In this tutorial, we shall learn about magic method.
It is a bit confusing at first, but you will get accustomed to it eventally.
"""

print([1,2,3,]+[4,5])
try:
    print([1,2,3,4]-[3,4])
except TypeError as e:
    print(str(e))

# we see that the list object has + means concatenation
#    but, it does not have any operation like -

# this is since, any magic method for - is not defined in list object class
# magic methods are some methods defined in classes, so that
#if we have some operand between two or more objects of a class
# then the method is called instead, i.e. the operand is mapped with the method
# for example...  + is mapped as __add__ method


"""
Let us look at a list of magic methods:

Operator                 Method
+                    object.__add__(self, other) 
-                    object.__sub__(self, other)
*                    object.__mul__(self, other) 
//                   object.__floordiv__(self, other)
/                    object.__truediv__(self, other)
%                    object.__mod__(self, other) 
**                   object.__pow__(self, other[, modulo]) 
<<                   object.__lshift__(self, other) 
>>                   object.__rshift__(self, other) 
&                    object.__and__(self, other)
^                    object.__xor__(self, other) 
|                    object.__or__(self, other) 

# in place operators

<operator>=          object.__i<method_for_original_operator>__(self, other)

#Unary operators

-                    object.__neg__(self) 
+                    object.__pos__(self) 
abs()                object.__abs__(self) 
~                    object.__invert__(self) 
complex()            object.__complex__(self) 
int()                object.__int__(self) 
long()               object.__long__(self) 
float()              object.__float__(self) 
oct()                object.__oct__(self) 
hex()                object.__hex__(self 

#comparison operators

<                    object.__lt__(self, other) 
<=                   object.__le__(self, other) 
==                   object.__eq__(self, other) 
!=                   object.__ne__(self, other) 
>=                   object.__ge__(self, other) 
>                    object.__gt__(self, other) 

"""

class A():

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return (len(self.value)*len(other.value))

    def __le__(self, other):
        return (self.value + other.value[::-1])

    def __invert__(self):
        return (self.value*2)


x = A('Hello')
y = A('Name')
print(x+y)
print(x<=y)
print(~x)

############################################
print()
#now, we shall take a look at __call__ method

class Polynomial:
    
    def __init__(self, *coefficients):
        self.coefficients = coefficients[::-1]
        
    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x** index
        return res


# call method turns the instances of the class into callables
# a constant function
p1 = Polynomial(42)

# a straight Line
p2 = Polynomial(0.75, 2)

# a third degree Polynomial
p3 = Polynomial(1, -0.5, 0.75, 2)

for i in range(1, 10):
    print(i, p1(i), p2(i), p3(i))

#these polynommial functions are object of the polynomial class


