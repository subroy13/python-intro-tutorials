"""
In this tutorial, we shall talk about use case of Metaclass
"""

# remember that we counted the number of function calls using decorator

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__
    return helper

@call_counter
def f():
    pass
print(f.calls)
for _ in range(10):
    f()
    
print(f.calls)

# However, in this tutorial, we are gonna write call_counter metaclass
print()
print()


class FuncCallCounter(type):
    """A metaclass which decorates all the methods of the subclass
       using call_counter as the decorator
    """

    @staticmethod
    def call_counter(func):
        def helper(*args, **kwargs):
            helper.calls += 1
            return func(*args, **kwargs)
        helper.calls = 0
        helper.__name__ = func.__name__

        return helper

    def __new__(cls, clsname, superclasses, attributedict):
        """ Every method gets decorated by call_counter by default"""
        for attr in attributedict:
            if not callable(attr) and not attr.startswith("__"):
                attributedict[attr] = cls.call_counter(attributedict[attr])

        return type.__new__(cls, clsname, superclasses, attributedict)

class A(metaclass = FuncCallCounter):

    def foo(self):
        pass

    def bar(self):
        pass

x = A()
print(x.foo.calls, x.bar.calls)
x.foo()
x.foo()
x.bar()
print(x.foo.calls, x.bar.calls)

























        
