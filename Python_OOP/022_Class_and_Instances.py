"""
In this tutorial, we shall 
"""

#First, we shall describe the static method

class Candy:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1  #counts how many candies has been produced

    def CandyNo(self):
        return Candy.__counter

x = Candy()
print(x.CandyNo())
y = Candy()
print(y.CandyNo())
try:
    print(Candy.CandyNo()) 
except:
    print('Error')
#an error is raised as the Candy.CandyNo needs an argument 'self' which is a
    # Candy object.

print()

#################################################
"""
We may go around by defining;

    def CandyNo():
        return Candy.__counter

In this case, the method cannot be called via an instance.
So we make use of 'static' method as follows:
"""

#   StaticMethods are functions that are defined in a class,
#   but can be used outside of the class, as this functions
#   does not require any self parameter to be passed on.

#   On the other hand, there is class_method, which takes argument cls
#   which is the class passing as parameter, then with that we can make
#   changes / call the classes static_methods


class Choco:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod   #this invokes a static decorator to the next function
    def Choco_count():
        return Choco.__counter

print(Choco.Choco_count())
x = Choco()
print(x.Choco_count())
y = Choco()
print(y.Choco_count())
print(Choco.Choco_count())

##########################################
print()

#however, there is another method called 'class' meethods
#these are like static methods, but only bound to a class


class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter
        

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())

print()
#######################################

#one use cases

class fraction(object):

    def __init__(self, n, d):
        self.numerator, self.denominator = fraction.reduce(n, d)
        
    @staticmethod
    def gcd(a,b):
        while b != 0:
            a, b = b, a%b
        return a

    @classmethod
    def reduce(cls, n1, n2):
        g = cls.gcd(n1, n2)
        return (n1 // g, n2 // g)

    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)


z = fraction(36,54)
print(z)   #print function by default asks __str__ method to fetch value as string










































