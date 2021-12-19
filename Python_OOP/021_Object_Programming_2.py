"""
We continue with our OOP tutorial
"""

#   Data Abstraction = Data Encapsulation + Data Hiding
#   Data Encapsulation:   It is a method of bundling some of the data in a class
#                         together, but that does not mean it is "hidden"

#   Data Hiding:    It is method of hiding the data, so that none can access or
#                   or see the data. It is meant to prevent some accidental changes
#                   in code.

#############################################
print("Encapsulation")

#encapsulation is acheived via two types of method,
#   1)Getter: It is used to fetch object values.
#   2)Setter: It is used to make changes to object values.

class Robot:
 
    def __init__(self, name=None, build_year=None):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot('" + self.name + "', " +  str(self.build_year) +  ")"

    def __str__(self):
        return "Name: " + self.name + ", Build Year: " +  str(self.build_year)
        
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
            
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    

x = Robot(build_year = '1998')
x.set_name("Charlie")
x.say_hi()
y = Robot()
y.set_name(x.get_name())
print(y.get_name())

#hence, based on this, we can give set method access to certain people,
# who can change the class attributes

#now, if we call str method on x, the usual str method is not called.
# but the functional method is called.

x_str = str(x)
print(x_str)
x_repr = repr(x)
print(x_repr)

#now, eval method cannot decipher x_str but can decipher x_repr
print(eval(x_repr))
try:
    print(eval(x_str))
except:
    print("Error")

############################################################
print()
print('Public, Protected and Private attributes')
#############################################################

"""
----Private attributes should only be used by the owner,
    i.e. inside of the class definition itself.
    it is denoted by     __   (double underscore) before the name of attribute.
----Protected (restricted) Attributes may be used, but at your own risk.
    Essentially, this means that they should only be used
    under certain conditions.
    it is denoted by    _   (single underscore) before the name of attribute.
----Public Attributes can and should be freely used.
    any name without  _  or __ is public.

    *** Nothing is completely private in python. We can access the private attribute
    by using   _<classname>__<attributename>
"""

class A():

    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

x = A()
print(x.pub)
print(x._prot)
try:
    print(x.__priv)
except AttributeError as e:
    print(str(e))

#observe that, the error message lies that A has no attribute __priv
#this is to hide the information that there is an existence of private attribute

print(x._A__priv)

#A complete Robot class with destructor and this hiding stuffs
print()
print('_______________________________________')
class Robot:
 
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year

    def __del__(self):
        #it is a destructor, which destroys the object and runs this __del__ method
        print('The robot has been destroyed')
    
    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")
            
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name    

    def set_build_year(self, by):
        self.__build_year = by
        
    def get_build_year(self):
        return self.__build_year    
    
    def __repr__(self):
        return "Robot('" + self.__name + "', " +  str(self.__build_year) +  ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)

x = Robot("Tik-tok", 1933)
print(str(x))
x.set_name("Mybot")
try:
    print(x.__build_year)
except AttributeError as e:
    print(str(e))
print(str(x))
del x






















