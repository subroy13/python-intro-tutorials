'''
In this program, we shall talk about string and their operations
'''

string = 'Hello World'  #string is like an array
print(string[0])
print(string[2:5])
print(string * 2)  #print string two times
print(string + 'TEST')   #concatenate strings
print(string.join('TEST')) #concatenate faster and efficiently
print(string.count('l'))    #count the number of times substring appears
print(string.index('l'))     #returns the first index of the substring
print(string[::-1])    #reverse the string object
print('-------------------------------------------------------')

print(int('a',base = 16))   #converts a character to integer on specified base
print(ord('a'))   #converts to unicode value of a character
print(chr(112))   #inverse of ord
print(hex(156))   #hexadecimal of 156, returns as a string with 0x at first
print(oct(156))   #octal of 156, returns as a string with 0o at first
print(bin(156))   #binary of 156, returns as a string with 0b at first
print('--------------------------------------------------------')

dictionary = dict([('name', 'Subhrajyoty'), ('age', 19), ('college','ISI')])  #argument must be a sequence of tuples (keys, values)
print(dictionary)

