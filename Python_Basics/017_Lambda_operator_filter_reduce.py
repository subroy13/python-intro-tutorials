"""
Lambda operators, filter, reduce and map
"""

#General syntax for lambda is quite simple:

#   lambda <argument list> : expression
# lambda is basically an inline function

mysum = lambda x, y : x+y

#this is same as;
#def mysum(x,y):
#   return x+y

print(mysum(3,4))

####################################
print('The advantage of lamda operator is evident in case of when it is used \
with map() function. Map() function takes two inputs')
######################################

# r = map(func, seq) which performs the following:
# def map(func, seq):
#   for i in seq:
#       result = func(i)
#       yield result

C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x+32, C))
print(F)

############################################
print('Lets see some good examples')
###########################################

a = [1,2,3,4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
print(list(map(lambda x,y,z: 2.5*x-y+4*z, a,b,c)))

###########################################
print()
print('Now some crash course on filtering')
###########################################

#filter function takes two arguments similar to map
#  filter(function, seq)

# def filter(function, seq):
#   filtered_list = []
#   for i in seq:
#       if function(i):
#           filtered_list.append(i)
#   return filtered_list

#############################################
fibonacci = [1,1,2,3,5,8,13, 21, 34, 55]
print('Some odd fibonacci numbers are: ', list(filter(lambda x: x%2,fibonacci)))
print('Some even fibonacci numbers are: ', list(filter(lambda x: x%2==0,fibonacci)))



###################################
print('Time for reducion')
##################################

#reduce takes two parameters,  reduce(function, seq), where the function also takes two parameters
# def reduce(function, seq):
#   while len(seq)>1:
#           seq[0]=function(seq[0], seq[1])
#   return seq[0]

#reduce is actually a function from functools that you need to import

from functools import reduce
print(reduce(lambda a,b: a if (a>b) else b, [47, 11, 42, 102, 13]))

#finding 49! 
print(reduce(lambda x,y: x*y, range(1,49)))



















