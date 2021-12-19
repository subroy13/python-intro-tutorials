"""
In this tutorial, we shall discuss about Metaclasses
"""
class Philosopher1:  
    def the_answer(self, *args):              
        return 42
    
class Philosopher2: 
    def the_answer(self, *args):              
        return 42
    
class Philosopher3: 
    def the_answer(self, *args):              
        return 42
    
plato = Philosopher1()
print(plato.the_answer())
kant = Philosopher2()
# let's see what Kant has to say :-)
print(kant.the_answer())

# All of these classes has same methods, hence,
# the above is a stupid way to implement this
print()
#An easy way to achieve this is to consider a base class
# and then introducing more subclasses
class Answers:
    def the_answer(self, *args):              
        return 42
    
class Philosopher1(Answers): 
    pass
class Philosopher2(Answers): 
    pass
class Philosopher3(Answers): 
    pass
plato = Philosopher1()
print(plato.the_answer())
kant = Philosopher2()
# let's see what Kant has to say :-)
print(kant.the_answer())
##################################################
print()
###################################################

# however, we may not know whether this method should be inside a class of not
# hence, it may be that we need to pass the argument whether we need the method

x = input("Do you need the answer? (y/n): ")
if x =="y":
    required = True
else:
    required = False

def the_answer(self, *args):
    return 42

#manager function
def augment_answer(cls):
    if required:
        cls.the_answer

augment_answer(Philosopher1)
augment_answer(Philosopher2)
augment_answer(Philosopher3)
plato = Philosopher1()
kant = Philosopher2()
# let's see what Plato and Kant have to say :-)
if required:
    print(kant.the_answer())
    print(plato.the_answer())
else:
    print("The silence of the philosphers")
#############################################
print()
#############################################

print("This is where metaclasses come in. Metaclasses are something\
 whose instances are classes")

class EssentialAnswers(type):

    def __init__(cls, clsname, superclasses, attributedict):
        if required:
            cls.the_answer = the_answer

    def __new__(cls, clsname, superclasses, attributedict):
        print("clsname: ", clsname)
        print("superclasses: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)


x = input("Do you need the answer? (y/n): ")
if x.lower() == "y":
    required = True
else:
    required = False

class Philosopher1(metaclass=EssentialAnswers): 
    pass
class Philosopher2(metaclass=EssentialAnswers): 
    pass
class Philosopher3(metaclass=EssentialAnswers): 
    pass
    
    
plato = Philosopher1()
print(plato.the_answer())
kant = Philosopher2()
# let's see what Kant has to say :-)
print(kant.the_answer())
########################################################
print()
####################################################
# metaclass can be used to create singleton classes, 
# singleton classes are classes which restricts the instantiation of the class to exactly one

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
    
class SingletonClass(metaclass=Singleton):
    pass
class RegularClass():
    pass
x = SingletonClass()
y = SingletonClass()
print(x == y)
#creates at max one instance, hence both x and y refers to the same
x = RegularClass()
y = RegularClass()
print(x == y)
























