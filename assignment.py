# function for volume of the sphere
import math

def vol(rad):
	return math.pi*(rad**3)

print(vol(2))

# find out if a num is in range

def ran_check(num, low, high):
	if num > low and num < high:
		return "its in range"
	else:
		return "not in range"

def ran_check_bool(num, low, high):
	return (num > low and num < high)

print(ran_check(2,3,7))

print(ran_check_bool(2,3,7))

