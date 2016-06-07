#simple square function test
def square(num):
	result = num**2
	return result

squareL = lambda num: num**2

print(squareL(2))

#checking for even
even = lambda num: num%2 == 0 

print(even(5))

# grans the first string character
first_char = lambda in_str: in_str[0]
print(first_char("hey"))

#reverse a string 
revS = lambda s: s[::-1]
print(revS("hey"))

'''
	this is not a usual way of using lambda function and 
	here it is just used for demo they would be almost used
	the same way we would use anonymus functions in JS
	these will be very handy when we deal with map(), filter() and reduce()
'''



