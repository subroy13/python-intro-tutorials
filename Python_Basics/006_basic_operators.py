"""
In this tutorial, we shall learn about built - in operators in python
"""

a = 10
b = 21
print('The following are arithmetic operations')
print(a+b)  #addition
print(a-b)  #substraction
print(a*b)   #multiplication
print(b/a)   #division upto float
print(b**a)   #exponentiation
print(b%a)   #modulus
print(b//a)   #floor or integer division
print('---------------------------------------------------------')

print('The following are comparison operators')
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print('---------------------------------------------------------')

print('The following are assignement operator')
print('=, += , -= , *= , /= , **= , //= , %= ')
print('--------------------------------------------------------')

print('The following are bitwise operators')
a = 60   # a in binary = 00111100
b = 13   # b in binary = 00001101
print(a&b,'in binary is', bin(a&b))   #bitwise and
print(a|b,'in binary is', bin(a|b))   #bitwise or
print(a^b,'in binary is', bin(a^b))   #bitwise xor
print(~a,'in binary is', bin(~a))   #bitwise not
print(a<<2,'in binary is', bin(a<<2))   #bitwise LEFT SHIFT
print(a>>3,'in binary is', bin(a>>3))   #bitwise RIGHT SHIFT
print('------------------------------------------------------------')

print('The following are logical operators')
print('and, or, Not')
print('-------------------------------------------------------------')

print('The following are membership operators')
print('in, not in')
print('------------------------------------------------------------')

print('The following are identity operators')
print('is, is not')   #is returns true if both side points to same object
print('-------------------------------------------------------------')























