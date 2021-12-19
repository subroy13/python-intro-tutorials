"""
This tutorial is on OOP (Object  Oriented Programming)
"""
#In object oriented programming, you can work with objects
#these objects are created in a factory, which are called 'class'
#'Class' is an object factory, whenever you call a class, it produces an instance of that class which is an object
# OOP has 4 main stuffs:
#   1) Encapsulation
#   2) Data abstraction
#   3) Polymorphism
#   4) Inheritence


#to see why python is OOP, conisder the following:

x = 42
print('42 is ',type(x))
y = 4.2
print('4.2 is ',type(y))
def f(x):
    return x+1
print('counting is ', type(f))

import math
print('imported math is ',type(math))

#python by default makes everything in a class
#whereas, in other OOP, we need to specify those classes

###############################################################
print()
##############################################################

#we can create user-defined class also

class Robot:
    pass

Charlie = Robot()
print('Charlie is a ', type(Charlie))

#observe that, it is <__main__.robot>. It means, the robot class is a subclass
# of the __main__ class, in which are program is currently working.

#we can add attributes to the object Charlie

Charlie.build_year = "1998"
Charlie.support = "Python"

print(Charlie.__dict__)  #this gives us a dictionary of all attributes of a class

Charlie.brand = 'Deepmind'

#now, if we try to access energy attribute of Charlie, we get an error
# we can prevent this as follows
print('Charlie has energy of ',getattr(Charlie,'energy',100),' units.')
#                              getattr(object_name, attribute_name, <if not found, deafult value>

##################################################
print()
#################################################

#even funtions can have attributes

def f(x):
    f.counter = getattr(f, "counter", 0) + 1 
    return "Monty Python"
        
for i in range(10):
    print(f(i))
    
print(f.counter)

#####################################################
print()
####################################################

#now, we shall go for methods, which is essential to objects

def hi(obj):
    print("Hi, I am " + obj.name + "!")

Charlie.name = "Charlie"
hi(Charlie)

#on the other hand, we can now redefine the class Robot with this hi function

class Robot:
    say_hi = hi

x = Robot()
x.name = "Marvin"
Robot.say_hi(x)  #this say_hi is a method, which is particular to this Robot class
x.say_hi()  #this also works. In this case, the object x passes itself to the say_hi method


###########################################################
print()
##########################################################

class Robot:
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am "+self.name)
        else:
            print("Hi, I am a robot without a name.")

x = Robot()  #whenever robot class produces something, it calls the init method
x.say_hi()
y = Robot("Marvin")
y.say_hi()











































