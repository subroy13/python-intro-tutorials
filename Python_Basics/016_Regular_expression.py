"""
In this tutorial, we will talk about regular expression.
The term "regular expression", sometimes also called regex or regexp, is originated in theoretical computer science.
In theoretical computer science they are used to define a language family with certain characteristics, the so-called regular languages.
"""

s = "Regular expression is easily explained"
print("easily" in s)  #this 'in' is a regular expression

#regular expression is just 'abbreviating' some regularly used strings or expressions

import re
#a module based on regualr expressions

x = re.search("cat", "A rat and a cat can't be friends")
print(x)
y = re.search("cow", "A rat and a cat can't be friends")
print(y)

#the above simple code tries to find the substring "cat" or "cow" in the sentence
print()

#let's assume we want to recognize all three letter words that ends with 'at'
z = re.search(r".at", "A rat and a cat can't be friends")
print(z)  #here it finds its first match with the word 'rat'

############
print()
#################

#we can use character classes, with is represented by []
# for example,   r"M[ae][iyp]er" it denotes all possible combinations of strings like;
#                 M(a or e)(i or y or p)er
#i.e.             Maier, Mayer, Maper, Meier, Meyer, Meper.

"""
You might have realized that it can be quite cumbersome to construct certain character classes.
A good example is the character class, which describes a valid word character.
These are all lower case and uppercase characters plus all the digits and the underscore,
corresponding to the following regular expression: r"[a-zA-Z0-9_]" 

The special sequences consist of "\\" and a character from the following list: 


\d           Matches any decimal digit; equivalent to the set [0-9].

\D           The complement of \d.
             It matches any non-digit character; equivalent to the set [^0-9].

\s           Matches any whitespace character; equivalent to [ \t\n\r\f\v].

\S           The complement of \s.
             It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].

\w           Matches any alphanumeric character; equivalent to [a-zA-Z0-9_].
             With LOCALE, it will match the set [a-zA-Z0-9_] plus characters defined as letters for the current locale.

\W           Matches the complement of \w.

\b           Matches the empty string, but only at the start or end of a word.

\B           Matches the empty string, but not at the start or end of a word.

\\           Matches a literal backslash
"""

f = open("simpsons_phone_book.txt", "r")
for line in f:
    if re.search(r"J.*Neu", line):
        print(line.rstrip())
f.close()

#the above function returns the name and phone number of those name,
#starting with name J and surname being Neu
print()

################################
print()
################################

#the re.match() function checks the match only at the beginning of a string
#we can use re.search() method to check the beginning also, but in this case,
#we have to use beginning of the string character ^

s1 = "Mayer is a very common name"
s2 = "He is called Meyer but he isn't a German."
print(re.match(r"M[ae][iy]er", s1))
print(re.match(r"M[ae][iy]er", s2))
print(re.search(r"M[ae][iy]er", s2))
print(re.search(r"^M[ae][iy]er", s1))
print(re.search(r"^M[ae][iy]er", s2))

#let's change it a bit
print(re.search(r"^M[ae][iy]er", s2+"\n"+s1))
#but we can use re.MULLTILINE to treat every line as a new string
print(re.search(r"^M[ae][iy]er", s2+"\n"+s1, re.MULTILINE))
#however, multiline mode does not affect match method
print(re.match(r"^M[ae][iy]er", s2+"\n"+s1))

#######################################
print()
#####################################



##  A subexpression is grouped by round brackets and a question mark
##  following such a group means that this group may or may not exist.
##  With the following expression we can match dates like "Feb 2011" or February 2011:    
##  r"Feb(ruary)? 2011"

# there are 3 types of this expressions
#   ?  the group may or may not exist
#   *  the group could be of arbitrary length
#   +  the group appears atleast once


string = "<composer>Wolfgang Amadeus Mozart</composer>\n<author>Samuel Beckett</author>\n<city>London</city>"
for i in string.split('\n'):
    res = re.search(r"<([a-z]+)>(.*)</\1>", str(i))  #here \1 is the referenced word in between < and >
    print(res.group(1) + ": " + res.group(2))


########################
print("Now the major part of seperating german post codes from the file")
####################

with open("german_post_code.txt") as fh_post_codes:
    codes4city = {}
    try:
        for line in fh_post_codes:
            res = re.search(r"[\d ]+([^\d]+[a-z])\s(\d+)", line)
            if res:
                city, post_code = res.groups()
                if city in codes4city:
                    codes4city[city].add(post_code) 
                else:
                    codes4city[city] = {post_code}
                    
    except Exception as e:
        print(str(e))



with open("largest_cities_germany.txt") as fh_largest_cities:
    try:
        for line in fh_largest_cities:
            re_obj = re.search(r"^[0-9]{1,2}\.\s+([\w\s-]+\w)\s+[0-9]", line)
            city = re_obj.group(1)
            print(city, list(codes4city[city])[:10])
            
    except Exception as e:
        print(str(e))
















































    
