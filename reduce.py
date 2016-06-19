import functools

'''
Reduce is a builtin function which takes a sequence and produces one output
It takes two values and applies function to it and then store it as first value and applies function to the new value
Syntax:
	reduce(function, sequence)

	let's say we have a list "numbers" [a,b,c,d] and we want to apply function "add" to get sum of the list
	
	def add (a,b):
		return a + b
	
	output_sum = reduce(add, numbers)

	so what is happening here?

	imaging this 
	----------------------------------
	a
	b 	sum1 = [a+b]
	c 	sum2 = [sum1 + c]
	d 	sum3 = [sum2 + d]

	output sum3
	-----------------------------

'''

def add(a,b):
	return a + b

stuff = [1,2,3,4,5]

output_sum = functools.reduce(add, stuff)

print(output_sum)
#15


# the largest number
def find_max(a,b):
	if a > b:
		return a
	else:
		return b

print(functools.reduce(find_max,[1,2,3,5,2,34,2,3,2]))




