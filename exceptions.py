def get_number():
	try:
		num = int(input("your number:"))
	except:
		print("not a number")
		get_number()
	else:
		print("square is: ")
		print(num**2)

get_number()