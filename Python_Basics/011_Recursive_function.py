"""
In this tutorial, we are gonna talk about recursion and memory
"""

from timeit import Timer

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib(n-1) + fib(n-2))


def fibi(n):
    old, new = 0, 1
    if n==0:
        return 0
    for i in range(n-1):
        old, new = new, old+new
    return new


memo = {0:0, 1:1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1)+fibm(n-2)
    return memo[n]




for i in range(1,41):
	s = "fibm(" + str(i) + ")"
	t1 = Timer(s, "from __main__ import fibm")
	time1 = t1.timeit(3)
	s = "fibi(" + str(i) + ")"
	t2 = Timer(s, "from __main__ import fibi")
	time2 = t2.timeit(3)
	s = "fib(" + str(i) + ")"
	t3 = Timer(s, "from __main__ import fib")
	time3 = t3.timeit(3)
	print("n=%2d, fibm: %8.6f, fibi:  %7.6f, fib: %8.6f" % (i, time1, time2, time3))

