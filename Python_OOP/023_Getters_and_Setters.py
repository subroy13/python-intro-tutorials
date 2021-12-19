"""
In this tutorial, we will talk about Getter and Setters.
"""

#given a private variable, we cannot access it from outside the class
# so we introduce two functions, one getter and one setter,
# with getter, we get the value of private attribute
# with setter, we set the value of private attribute

class A:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name_new):
        if len(name_new)<=10:
            self.__name = name_new
        else:
            print('Give me another value')

x = A('first')
y = A('second')
print(x.get_name())
print(y.get_name())
print()
x.set_name('New first')
print(x.get_name())
x.set_name('My new first value')


##########################################
print()
##########################################

#The above is a JAVA way to do things

#a Pythonic way to do these stuffs is different, let's consider the following:

# Here, we innclude property. Property is a decorator , which is put before
# another function, so that, if we access the attribute with the same name
# as the function name, the function is called instead

class P:

    def __init__(self,x):
        self.x = x    #defining a public attribute

    @property   
    def x(self):    #this is a get method
        return self.__x

    @x.setter
    def x(self, val):
        if val<0:
            self.__x =0
        elif val>1000:
            self.__x = 1000
        else:
            self.__x = val

    #this defines a setter method that allows you to set x with specific rule

a = P(1002)
print(a.x)   #here, the method or property a.x() is called instead 
a.x = -12   #however, now the setter method is called as we are trying to set some value to this

#the way the above works is:
#   -12 creates a <__main__.int> object
#   a.x is called, it calls the property method by default, which returns self.__x
#   then, this self.__x = -12 is called
#   so, the setter method is called, and this self.__x value is verified to be in
#       range of (0,1000) and set the value 

print(a.x)

"""
This is actually what's happening:

class P:

    def __init__(self,x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(get_x, set_x)
"""




























