raw_input = input("Enter which output you like to get: 1.Sets  2.Lists  3.Dictionaries  4.Tuples\n")
raw_input = int(raw_input)
if raw_input == 1:
        example_set = set([28, True, 2.1728, "Helium"]) #this creates a set
        print("The initial set is given by", example_set) #in set, order of elements does not matter
        example_set.add("Sun")
        example_set.add(28)
        print("The set at stage2 is given by", example_set) #in set, you cannot add duplicates
        example_set.remove(True)
        print("The set at stage3 is given by", example_set)
        #to know more functions related to sets, try dir(example_set)
elif raw_input ==2:
        #lists are sets where order matters
        example_list = list() #this creates an empty list
        example_list = [17, 13, 2, 5, 7, 3] #can use [] also to create lists
        print("The initial list is given by",example_list)
        example_list.append(19)
        print("The list at stage2 is given by", example_list)
        print("The list is:")
        for k in range(0,len(example_list)):
                print(example_list[k])
        print("The list in backwards is:")
        for k in range(1, 1+len(example_list)):
                print(example_list[-k])
        #list can contain duplicates, can even contain other lists
        example_list.reverse()
        print("The list in backwards is:", example_list)
elif raw_input == 3:
        #dictionaries are functions / mappings between two lists
        example_dict = {"user": 'XYZ', "id": 13, "message": "D5 E5 C5", "location":[44.590533, -104.71556]}
        #the field names are called keys (pre-images)
        #the images of fields are called values
        type(example_dict)
        print("The dictionary is", example_dict)
        key = list(example_dict.keys()) #returns the dict_keys list and make it a normal list
        key.append('language')
        for k in key:
                print(example_dict.get(k, "None"))

elif raw_input == 4:
        #tuples are non-modifiable lists that is fast to use and have smaller sizes
        example_tuple = (1,4,9,16,25,36)
        print("The tuple is",example_tuple)
        emptytuple = ()
        test1 = ("a") #this is just a string
        test2 = ("a",) #this is a tuple
        print("Test1 is a ",type(test1), "And Test2 is a ",type(test2))
        survey = ("Oliver",27,"India",True)
        Name, age, country, knows_python = survey #this unpacks the values
        print(Name, "of age", age, "from", country, "knows python -- is a ", knows_python, "statement")
        
input()
        
