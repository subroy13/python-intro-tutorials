"""
Decorators is any callable object which is used to modify a function or a class
"""

#first step

def succ(x):
    return x+1

successor = succ
print(successor(10))
print(succ(10))

#Both succ and successor references to the same function

del succ  #delete the succ function
print(successor(10))  #the successor function still holds the reference

#####################################
print()
####################################

#defining functions inside of function

def f():

    def g():
        print("Hi!, It's me")
        print("Thanks for calling")

    print("This is function f")
    print("I am calling g now")

    g()


#call the function f now
f()

#####################################
print()
####################################



def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
    
def f(func):
    print("Hi, it's me 'f'")
    print("I will call %s now"%(func.__name__))
    func()
          
f(g)


##################################
print()
#################################

#function can return functions

def f(x):
    def g(y):
        return y**x
    return g

nf1 = f(2)
nf2 = f(5)

print(nf1(4))
print(nf2(4))


######################################
print()
######################################

#a simple decorator

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo("Hi")
    
print("We now decorate foo with f:")
foo = our_decorator(foo)   #foo has been updated with our_decorator function

#this above line is the decorator working
#instead of this, we can simply use    @our_decorator
#however this decorator decorates every other function in the code that takes one parameter


print("We call foo after decoration:")
foo("Hi")


###################################
print("Uses of Decorators")
###################################

# checking validity of calling a function

def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            print("Argument is not an integer")
    return helper
    
@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1,10):
	print(i, factorial(i))

print(factorial(-1))



print()

# counting function calls

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1

@call_counter
def mul1(x, y=1):
    return x*y + 1

print(succ.calls)
for i in range(10):
    succ(i)
mul1(3, 4)
mul1(4)
mul1(y=3, x=2)
    
print(succ.calls)
print(mul1.calls)


#######################################
print()
######################################



#now we talk about using decorators in class

class A:

    def __init__(self):
        print('An instance of A was initialized')   #this works when instance is created

    def __call__(self, *args, **kwargs):
        print("Arguments are : ", args, kwargs)   #this works when that instance is called

#this __call__ method is a decorator
#now when we create an instance of A
x = A()
print("Now calling the instance x: ")
x(3, 4, x = 11, y = 10)
print("Let's call it again: ")
x(3, 4, x = 2, y = 3)

####################################
print()
##################################

class Fibonacci:
    def __init__(self):
        self.cache = {}
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]

fib = Fibonacci()

for i in range(15):
    print(fib(i), end=", ")

##########################################
print()
#########################################


















































































