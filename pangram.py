import string
# pangram are sentences which have all the alphabets. how do we check that?


alphabets = string.ascii_lowercase


#solution1
def ispangram1(str):
	notfound = []
	for i in alphabets:
		if i not in str:
			notfound.append(i)
	if len(notfound) > 0:
		#'Point({self.x}, {self.y})'.format(self=self)
		print("not an pangram\ndidn't find {number} alphabets".format(number =len(notfound)))
	else:
		print("it is an pangram")

ispangram1("a quick brown fox jumps over the lazy dog")