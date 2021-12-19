"""
In this tutorial we shall learn about list comprehension.
"""

#suppose we want to create pythagorean triplets

pythagorean_triplets = [(x,y,z) for x in range(1,30) for y in range(1,30)\
                        for z in range(1,30) if x**2+y**2==z**2]
print(pythagorean_triplets)


####################################
print()
###################################

#however, if we want to return a generator, then we have to use () instead of []

squares = (x**2 for x in range(20))
print(squares)
for _ in range(10):
    print(next(squares))


#####################################
print()
####################################

print('Implementing Seive of Eratosthenis')

def sieve(n):
    '''returns primes upto n'''
    nonprimes = [j for i in range(2, int(n**0.5)) for j in range(i**2, n, i)]
    primes = [x for x in range(2,n) if x not in nonprimes]
    return primes

print(sieve(1000))

####################################
print()
####################################

























