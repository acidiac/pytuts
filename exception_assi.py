#exception_assi
for i in ['a',3,'c']:
	try:
		val = i**2
	except:
		print("not a number")
	else:
		print (val)

def ask():
	while True:
		try:
			val = int(input("enter a number"))
		except:
			print("you didn't enter a number, try again!")
		else:
			break
	print(val**2)

ask()
			

