class Cylinder(object):
	pi = 3.14

	def __init__(self, height=1, radius=1):
		self.height = height
		self.radius = radius

	def volume(self):
		h  = self.height
		r  = self.radius
		pi = self.pi
		return pi*(r**2)*h

	def surface_area(self):
		h  = self.height
		r  = self.radius
		pi = self.pi
		top = pi * r**2
		return (top*2)+ (2*pi*r*h)


nc = Cylinder(4,6)

print(nc.volume())
print(nc.surface_area())

