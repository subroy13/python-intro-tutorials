def prime_check(n):
	"""This function checks whether a given number is prime or composite"""
	for k in range(2,int(n**0.5)):
		if n%k==0:
			return 0 #since n is divisible by k and hence composite
	return 1 #since n is nnot divisible by any k and hence prime

raw_input = input("Please enter a number: ")
while raw_input:
        number = int(raw_input)
        if number <=1:
                print("The entered number is neither prime nor composite")
        elif number==2:
                print("The entered number is prime")
        else:
                primality = prime_check(number)
                if primality==0:
                        print("The entered number is composite")
                else:
                        print("The entered number is prime")
                        
        raw_input = input("Please enter a number: ")
