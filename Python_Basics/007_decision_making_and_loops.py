"""
Python decision making and loops
"""
person = str(input('Nationality?'))
if person == ('Indian' or 'indian'):
    print('Namaste!')
elif person == ('Japanese' or 'japanese'):
    print('Arigato Hoshaimasta')
else:
    print('You seem to be neither Indian nor Japanese.')
    print('So, we have to speak in English')
    


"""Using ternary if"""

"""
In C, we have

max = (a>b)?a:b;

In python, we have

max = a if (a>b) else b
"""

#Now for loops
"""
Python has these three channels as well:
-----standard input
-----standard output
-----standard error
They are contained in the module sys. Their names are:
-----sys.stdin
-----sys.stdout
-----sys.stderror
"""

import sys

text = ""
while 1:
    c = sys.stdin.read(1)
    text = text + c
    if c == '\n':
        break

print('Input: %s' %text)

#The above program takes input from the standard input character by character and prints it



###Number guessing game
import random
n = 50
to_be_guessed = int( n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you are giving up")
        break
else:
    print("Congratulation. You made it!")



























