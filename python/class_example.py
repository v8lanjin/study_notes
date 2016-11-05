class A:
	pass

class B(A):
	pass

print(issubclass(B,A))

b1 = B()
print(isinstance(b1, B))

print(isinstance(b1, A))

class C:
	def __init__(self, x = 0):
		self.x = x
c1 = C()
print(hasattr(c1, 'x')) # notice the attr name is a string
print("c1's x = " + str(getattr(c1, 'x')))
print("c1's y = " + str(getattr(c1, 'y', "sorry there is no attr named y")))

print("c1 has attr x? " + str(hasattr(c1, 'x')))

setattr(c1, 'y', 1)
print("after setattr")
print("c1's y = " + str(getattr(c1, 'y', "sorry there is no attr named y")))

delattr(c1, 'y')
print("after delattr")
print("c1's y = " + str(getattr(c1, 'y', "sorry there is no attr named y")))


# property()
class D:
	def __init__(self, size = 10):
		self.size = size
	def getSize(self):
		return self.size
	def setSize(self, size):
		self.size = size
	def delSize(self):
		del self.size
	x = property(getSize, setSize, delSize)

d = D()
print(d.x)
d.x = 20
print(d.x)
print(d.size)
del d.x
try:
	print(d.size)
except AttributeError as e:
	print("there is no attr named size")
