'''
this is important concept and would be important if we want to go further
anytime we declare a variable or object its get assigned to namespace which is
made available to part of your code which has access to it

order of variable search ::: Local---> Enclosing local functions ---> Global ---> Built-in

'''
# local and enclosing scope
def localfunc():
	# message here is local to localfunc
	message = " hi from local function!"
	def inside():
		#message here is in enclosing scope
		message_in = "enclosing function > "
		print (message_in + message)
	inside()

localfunc()
	





