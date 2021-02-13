# write a program that prints the number from 1 to 100
# But for multiples of three prints "Fizz" instead of the number
# and for multiples of five print "Buzz"
# for multiples of both three and five  prints "FizzBuzz"



count_list = range(1,101)
for i in count_list:
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 5 == 0:
		print("Buzz")
	elif i % 3 == 0:
		print("Fizz")
	else:
		print(i)
		
	 	