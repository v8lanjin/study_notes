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


# =====================================
import time as t

class MyTimer():
	def __init__(self):
		self.prompt = "please init"
		self.unit = ['y', 'mon', 'd', 'h', 'min', 's']
	def start(self):
		self.startTime = t.localtime()
		# print("starting timer...:" + str(self.startTime))
		self.prompt = "please stop timer at first"
	def stop(self):
		self.stopTime = t.localtime()
		# print("stoping timer... :" + str(self.stopTime))
		self._calc()

	def _calc(self):
		self.lasted = []
		self.prompt = "last:"
		if not self.stopTime:
			return self
		for i in range(6):
			self.lasted.append(self.stopTime[i] - self.startTime[i])
			if self.lasted[i] != 0:
				self.prompt += ' ' + str(self.lasted[i]) + self.unit[i]
		if self.prompt == "last:":
			self.prompt += " 0s"
		for i in range(5):
			if self.lasted[i] < 0:
				self.lasted[i] + 60
				self.lasted[i+1] -= 1
			elif self.lasted[i] >= 60:
				self.lasted[i] -= 60
				self.lasted[i] += 1
		print(self)

	def __add__(self, other):
		if not self.lasted and not other.lasted:
			lasted = []
			for i in range(6):
				lasted.append(self.lasted[i] + other.lasted[i])
			for i in range(5):
				if self.lasted[i] >= 60:
					self.lasted[i] -= 60
					self.lasted[i] += 1
			return lasted
		else:
			print("please init all the args")
	def __sub__(self, other):
		pass

	def __str__(self):
		return self.prompt
	#def __repr__(self):
	#	pass
	__repr__ = __str__

m1 = MyTimer()
print(m1)

m1.start()
print(m1)
m1.stop()
t.sleep(1)
m1.stop()

m2 = MyTimer()
m2.start()
m2.stop()
print(m1 + m2)