"""
In this tutorial, we will use memoization using decorators
"""

#In memoization for fibonacci series, we discarded the recursive function and
#used a new version of function
#in this, we used the same recursive function and decorate it with another function

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x]=f(x)
        return memo[x]
    return helper


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

fib = memoize(fib)# instead onne could use @memoize
print(fib(40))


###############################
print()
###############################

#here we use a class as memoization decorator

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(100))





















