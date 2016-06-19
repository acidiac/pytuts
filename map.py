'''
Map is a built-in function which literally does what the name says, it maps a function to an iterable.
Syntax:
	map(function, iterable) 
	the above syntax will return an object with result of outputs from the iterable(list, set..). This can
	be converted into a list by simply using the list() function.

'''



def sft_to_sqm(val):
	'''
		square feet area into square meters
	'''
	return (val * 0.09290)

area_sft = [23,34,45,67,73,11,89,113]

area_sqm = list(map(sft_to_sqm, area_sft))

print(area_sqm)


# map using lambda expression

new_area = list(map(lambda area: area*0.0929, area_sft))

print(new_area)

