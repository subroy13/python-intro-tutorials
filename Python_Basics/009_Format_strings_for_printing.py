"""
In this tutorial we shall observe the bahaviour of format string
"""

#the basic of the format string is:    %[flag][width][.precision]type
#flag denotes the precedding character of the number like 0X, or 00x, or 0b
#width denotes the max width (number of character) it should print for the number
#.precision means the number of digits after decimal, without violating width
#type is the datatype or number type

print('10.3f of 356.08977', "%10.3f"%(356.08977))
print('6.3f of 356.08977', "%6.3f"%(356.08977))
print('10.3e of 356.08977', "%10.3e"%(356.08977))
print('10o of 25', "%10o"%(25))  #o = octal
print('10.5o of 25', "%10.5o"%(25))
print('5.4x of of 47', "%5.4x"%(47))    #x = hexadecimal

print('#5X of 47', "%#5X"%(47))   # #flag means to give 0x, 0o, or 0b based on the number type
print('05X of 47', "%05X"%(47))   # 0 flag means the nummber is padded with 0 in front
print('+d of 42', "%+d"%(42))     # + adds a +/- sign in the front
print('+d of -42', "%+d"%(-42))



print("Only one percentage sign: %%" %() )
print("Only one percentage sign: %")



##############


# Python has another way to format string output, using .format function
#It is also called positional argument

print("First argument: {0}, second one: {1}".format(47,11))
print("Second argument: {1}, first one: {0}".format(47,11))
print("Second argument: {1:03d}, first one: {0:7.2f}".format(47.42,11))

print("Art: {a: 05d}, Price: {p: 8.2f}".format(a=453, p = 59.058))


data = {'province':'India', 'capital':'New Delhi'}
print("The capital of {province} is {capital}".format(**data))

#an extended version of this is;
capital_country = {"United States" : "Washington",  
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam",
                   "India" : "New Delhi",
                   "Japan" : "Tokyo"}

print("Countries and their captials:")
for c in capital_country:
    format_string = c + " : {" + c + "}"
    print(format_string.format(**capital_country))





















