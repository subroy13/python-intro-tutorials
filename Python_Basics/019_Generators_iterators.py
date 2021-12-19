#Generators are different than functions, functions always start
#execution from beginning, while generators saves the last checkpoint

def gen():
    yield 1
    raise StopIteration

g = gen()
print(next(g))  #now calling next on g with raise stopiteration
try:
    print(next(g))
except StopIteration:
    print('StopIteration')

###############################
print()
#################################

#generators does not only send objects but can receive objects too

def simple_coroutine():
    print('Coroutine initiated')
    x = yield
    print('Coroutine received: ',x)

cr = simple_coroutine()
print(next(cr))
try:
    print(cr.send('Hi'))
except StopIteration as s:
    print(str(s))

#############################################
# we can create infinte loop to make an interactive shell also
#############################################
#send method sends the value to the generator and also yields the value by the generator
# send method sends the value to the variable lying left hand side of yield

def infinite_looper(objects):
    count = 0
    while True:
        if count >= len(objects):
            count = 0
        message = yield objects[count]
        if message!=None:
            count = 0 if message < 0 else message
        else:
            count += 1

x = infinite_looper('A string with some words')
print(next(x))
print(x.send(9))
print(x.send(12))

#############################################
print()
############################################
#decorating generators

from functools import wraps

def get_ready(gen):
    """
    Decorator: gets a generator gen ready 
    by advancing to first yield statement
    """
    @wraps(gen)
    def generator(*args,**kwargs):   
        g = gen(*args,**kwargs)   
        next(g)   
        return g   
    return generator

@get_ready

def new_looper(objects):
    count = 0
    while True:
        if count >= len(objects):
            count = 0
        message = yield objects[count]
        if message!=None:
            count = 0 if message < 0 else message
        else:
            count += 1
            

x = new_looper("abcdef")
print(next(x))
print(next(x))

##############################################
 # from python 3.3, we can use 'yield from' method to yield from a generator in one line

 #like;    yield from [1,2,3,4,5]     generates the sequence of 1,2,3,4,5

#for demonstration

def gen1():
    for char in "Python":
        yield char
    for i in range(5):
        yield i

def gen2():
    yield from "Python"
    yield from range(5)

g1 = gen1()
g2 = gen2()
print("g1: ", end=", ")
for x in g1:
    print(x, end=", ")
print("\ng2: ", end=", ")
for x in g2:
    print(x, end=", ")
print()

######################################################

#now, we shall show the use of recursive generators

def permutations(items):
    n = len(items)
    if n==0:
        yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]]+cc

for p in permutations(['a','b','c','d']):
    print(''.join(p))






















 































