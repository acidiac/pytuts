import functools
'''
Use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list.
The function will have an input of a string, and output a list of integers.
'''
def word_lengths(phrase):
	print(list(map(len, phrase.split(" "))))
    
#word_lengths('How long are the words in this phrase')

'''
Use reduce to take a list of digits and return the number that they correspond to. Do not convert the integers to strings!
'''
def digits_to_num(digits):
	return(functools.reduce(lambda a,b : a*10+b, digits))
#print(digits_to_num([3,4,3,2,1]))

'''
Use filter to return the words from a list of words which start with a target letter.
'''


def filter_words(word_list, letter):
    
    return list(filter(lambda word: word[0]==letter,word_list))


l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print(filter_words(l,'h'))

'''

Problem 4
Use zip and list comprehension to return a list of the same 
length where each value is the two strings from L1 and L2 concatenated together 
with connector between them. Look at the example output below:

'''

'''

Problem 5
Use enumerate and other skills to return a dictionary which has the values 
of the list as keys and the index as the value. You may assume that a value 
will only appear once in the given list.

'''

'''
Problem 6
Use enumerate and other skills from above to return the count of the number 
of items in the list whose value equals its index.
'''
    