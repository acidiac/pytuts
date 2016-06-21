'''
Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list.
The function will have an input of a string, and output a list of integers.
'''
def word_lengths(phrase):
	print(list(map(lambda x : len(x), phrase.split(" "))))
    
word_lengths('How long are the words in this phrase')