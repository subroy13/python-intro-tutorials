"""
In this tutorial, we shall discuss about parameter argument.
"""

#When calling a function, one should pass the parameter along with the information
#about the environment. This helps the function to return to the environment
#from where it has been called.


#Call by value:
#the most common strategy to call parameters in function is call by its value.
#the function makes a copy of the passed parameter along with its value.

#Call by Reference:
#another is to call by reference, where the function takes the input as the reference
#to the parameter/ object it passed, it does not make another copy.
#hence, any changes made to the object inside the function, retains after returning from the function


#Python makes use of call by Object Reference for mutable objects passed as parameters
#while if we pass immutable objects like string, integer or tuples, it acts as call by value method
#this is often refered as 'Call by Object'



def ref_demo(x):
    print("x=",x," id=",id(x))
    x = 42
    print("x=", x, " id=", id(x))


x = 9
print(id(x))
ref_demo(x)
#the object reference is passed
#the object should have been mutated in the function, but it is not as it is integer
#now, after coming back let us print id of x again
print(id(x))


##########consider another example
print()
print()
def no_side_effects(cities):
    cities = cities + ["Delhi", "Bengaluru"] #here we make a local copy of cities by adding two more cities in the passed cities object ref
    print(cities)

locations = ["Kolkata", "Chennai", "Mumbai"]
no_side_effects(locations)
print(locations)


#however it changes if we use assignment operator
print()
print()
def side_effects(cities):
    cities += ["Delhi", "Bengaluru"]   #it acts in place
    print(cities)

locations = ["Kolkata", "Chennai", "Mumbai"]
side_effects(locations)
print(locations)
print()

locations = ["Kolkata", "Chennai", "Mumbai"]
side_effects(locations[:])
print(locations)





































