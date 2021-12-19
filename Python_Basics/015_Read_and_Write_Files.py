"""
In this tutorial, we are gonna open files and read from them
"""

#to create a file, or read or write it,
#one needs to open a connection to the file first
#then we can work with the connection and each time the connection is modified, the file gets updated

f = open("example.txt", "w")  ##opening in write 'w' mode, if we want, we can specify buffer to limit writing and reading speed

f.write("This is an example text.\nThis is a new line. I can continue this line,\nor make a new line.")
f.close()   #this is really important to close the file connection before accessing the file via anything else (third party software)

fobj_in = open("example.txt", "r")  #opening in read mode
fobj_out = open("example2.txt","w")
i = 1
for line in fobj_in:
    print(line.rstrip())   #rstrip removes strip of blank space, printing the string without spaces between new printing
    fobj_out.write(str(i) + ": " + line)
    i = i + 1
fobj_in.close()
fobj_out.close()

#################
print()
#################

#we can read the files in one go

with open("example.txt", "r") as myfile:
    mywritings = myfile.readlines()
    myfile.close()

print(mywritings)

#############################
print()
#############################

fh = open("Sample_text.txt")
print(fh.read(15))  #read 15 characters from current cursor position
print(fh.seek(fh.tell() -6)) # set the current position 6 characters to the left:
print(fh.read(5))

# now, we will advance 29 characters to the  
# 'right' relative to the current position:
print(fh.seek(fh.tell() + 29))  #returns the current position
print(fh.read(10))



############################
print()
###########################

#now we will discuss about pickle

import pickle
#this module helps to save objects to a pickle file

with open('pickle_example.pkl', 'wb') as f:
    #'wb' denotes the write binary mode which is writing the object in machine language
    languages = ["English", "Hindi", "Bengali",  "French", "German"]
    pickle.dump(languages, f)
    f.close()

with open('pickle_example.pkl', 'rb') as g:
    lan = pickle.load(g)
    g.close()

print(lan)

########################################
print()
######################################

#problem with pickle is that when saving a dictionary, we may not want to load the whole dictionary again, but some values of it
#so we have 'shelve'

import shelve
tele = shelve.open("MyPhoneBook")
tele["Mike"] = {"first":"Mike", "last":"Miller", "phone":"4689"}
tele["Steve"] = {"first":"Stephan", "last":"Burns", "phone":"8745"}
tele["Eve"] = {"first":"Eve", "last":"Naomi", "phone":"9069"}
tele.close()

book = shelve.open("MyPhoneBook")
print(book["Steve"]["phone"])






























