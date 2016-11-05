# __init__(self[, ...])
class Rectangle:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
	def getPeri(self):
		return (self.w + self.h) * 2
	def getArea(self):
		return self.w * self.h
r = Rectangle(0, 0, 5, 7)
print(r.getPeri())
print(r.getArea())

#def __new__(cls[, ...]):
class CapStr(str):
	def __new__(cls, string):
		string = string.upper()
		return str.__new__(cls, string)
s = CapStr("hello")
print(s)


# __del__(self)
class delDemo:
	def __init__(self):
		print("delDemo init")
	def __del__(self):
		print("delDemo del")

dd = delDemo()
cc = dd
xx = dd

del xx
del cc
print("==========")