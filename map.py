'''
Map is a built-in function which literally does what the name says, it maps a function to an iterable.
Syntax:
	map(function, iterable(s)) 
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
#[2.1367, 3.1586, 4.180499999999999, 6.2242999999999995, 6.7817, 1.0219, 8.2681, 10.4977]



# map using lambda expression

new_area = list(map(lambda area: area*0.0929, area_sft))

print(new_area)
# [2.1367, 3.1586, 4.180499999999999, 6.2242999999999995, 6.7817, 1.0219, 8.2681, 10.4977]

# we can use map with more than one iterable
# this is quite an stupid example but I think this makes it a bit more clearer
withdrawals = [100,15,23,35]
deposits 	= [200,45,12,450]
months = ["jan","feb","mar","apr"]

def acc_state(withdraw, deposit, month):
	balance = deposit - withdraw
	return ("month [%s], Monthly Balance: %d " %(month,balance))

statement = list(map(acc_state, withdrawals,deposits,months))
print(statement) # this is not really a good practice but for now lets see what it does..
# ['month [jan], Monthly Balance: 100 ', 'month [feb], Monthly Balance: 30 ', 'month [mar], Monthly Balance: -11 ', 'month [apr], Monthly Balance: 415 ']




