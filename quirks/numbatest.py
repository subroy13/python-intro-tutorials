########################
# A Program to showcase basic numba compilation vs numpy
########################
from numba import jit
import numpy as np
from timemeasure import measure_time

x = np.random.rand(10000).reshape(100, 100)

@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def go_fast(a): # Function is compiled to machine code when called the first time
    trace = 0.0
    for i in range(a.shape[0]):   # Numba likes loops
        trace += np.tanh(a[i, i]) # Numba likes NumPy functions
    return a + trace              # Numba likes NumPy broadcasting

def go_slow_np(a):
    trace = 0.0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace

def go_fast_np(a):
    return a + np.tanh(np.diag(a)).sum()

if __name__ == "__main__":
    print('Method 1', measure_time(lambda: go_slow_np(x), 1000))
    print('Method 2', measure_time(lambda: go_fast_np(x), 1000))
    print('Method 3', measure_time(lambda: go_fast(x), 1000))

# from timeit import timeit

# print(timeit('go_slow_np(x)', number=1000, globals=globals()))
# print(timeit('go_fast_np(x)', number=1000, globals=globals()))
# print(timeit('go_fast(x)', number=1000, globals=globals()))

    