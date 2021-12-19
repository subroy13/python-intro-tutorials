"""
In this tutorial, we will undertand the deep copy and shallow copy
"""
x = 3
y = x  #y has same reference to the object x
print(id(x), id(y))  #so their id's are same

y = 4  #now y is assigned to hold a new object. and it does not modify the obejct x
print(id(x), id(y), x, y)  #the value of x is not changed

#this happens as y is a shallow copy of the object x, y works like just a reference for object x

#########let's see what happens when we want to copy a list.
print()


country = ['India', 'China', 'America']
country2 = country
print(id(country), id(country2))

country2[1] = 'England'
print(id(country), id(country2), country, country2)

country2 = ['France', 'Japan', 'Italy']
print(id(country), id(country2), country, country2)

#the reasonn for the above is that when creating a list, the list object country
#is a memory chunk that contains some refernce pointers to these lists elements
#when creating country2, it acts as a reference of the object country.
#now, changing country2[1] will pass though the refernce of country2 and tries to
#access its 1st element, which also happens to be the first element of country list.
#therefore, changing the string object to something ... after that, country list
#still holds the references to that string object as elements, so it also gets modified


#however, slicing allows us to get rid of it
country3 = country2[:]  #it creates another copy of the country2, not just a ref pointer
country3[0] = 'Turkey'
print(country3, country2)


##to explain more, conisder the example
lst1 = ['a','b',['ab','ba']]
lst2 = lst1[:]
lst2[0] = 'c'
lst2[2][1] = 'd'
print(lst1)
print(lst2)
print(id(lst1), id(lst2))


#####to make deepcopy, we need a module called copy, which comes with python

from copy import deepcopy

lst3 = deepcopy(lst1)
print(lst1, lst3, id(lst1), id(lst3))





















