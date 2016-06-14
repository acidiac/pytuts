class Line(object):
	def __init__(self, coor1, coor2):
		#coor are tuples (3,2)
		self.coor1 = coor1
		self.coor2 = coor2

	def __str__(self):
		x1,y1 = self.coor1
		x2,y2 = self.coor2
		return ("A line between (%d,%d) and (%d,%d)" %(x1,y1,x2,y2))


	def distance(self):
		#tuple unpacking
		x1,y1 = self.coor1
		x2,y2 = self.coor2
		print(x1, y1, x2, y2)
		return ((x2-x1)**2/(y2-y1)**2)**0.5

	def slope(self):
		x1,y1 = self.coor1
		x2,y2 = self.coor2
		return (y2-y1)/(x2-x1)


# testing the cases

new_line = Line((4,4),(1,0))

print(new_line)