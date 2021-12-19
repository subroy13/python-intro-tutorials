"""
In this tutorial, we aare gonna talk about functions
"""


#a function is like a production factory, you give some input, it outputs something

def farenheit(T_in_celsius):
    """This is called docstring. It contains information about your function
    For example, this function returns the temperature T in farenheit.
    If you call help function for this 'Farenheit' function, this docstring will show up"""

    return (((T_in_celsius * 9)/5)+32)


help(farenheit)

for t in [22.6, 25.8, 27.3, 29.8]:
    print(t ," : ", farenheit(t))



def mean(first, *values):
    """ *values mean that an arbitrary number of inputs can be placed.
    This function returns the arithmetic mean of given numbers"""
    total = (first + sum(values))
    return (total/(1+len(values)))

print(mean(89, 978, 72.90, 7.42, 83.2, 84.32))
print(mean(74, 21))
#it takes variable length input
