class MyInt(int):
	def __add__(self, other):
		print("Add operation:")
		return int.__add__(self, other)
		# return self + other
		# return int(self) + int(other)
	def __sub__(self, other):
		print("Sub operation:")
		return int.__sub__(self, other)

	# def __mul__(self, other):
	# def __truediv__
	# def __floordiv
	# def __mod__
	# def __divmod__
	# def __pow__
	# def __lshift__
	# def __rshift__
	# def __and__
	# def __xor__
	# def __or__

a = MyInt(10)
b = MyInt(20)
print(a + b)
print(a - b)

class rInt(int):
	def __rsub__(self, other):
		return int.__sub__(self, other)
a = rInt(8)
print(1 - a)

class rInt(int):
	def __rsub__(self, other):
		return int.__sub__(other, self)
a = rInt(8)
print(1 - a)