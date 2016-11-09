class Prop():
	def __init__(self):
		self.x = 0
	def getX(self):
		return self.x
	def setX(self, x):
		self.x = x
	def delX(self):
		del self.x

	p = property(getX, setX, delX)

p1 = Prop()
print(p1.x)

p1.p = 10
print(p1.p)
print(p1.x)



# __getattr__(self, name)
#__getattribute__
#__setattr__
#__delattr__

class C:
	def __getattribute__(self, name): # this method will be called when a attr be refered
		print("__getattribute__")
		return super().__getattribute__(name)
	def __getattr__(self, name):
		print("__getattr__")
		# return super().__getattr__(name)
	def __setattr__(self, name, value):
		print("__setattr__ " + name + ' ' + str(value))
		return super().__setattr__(name, value)
	def __delattr__(self, name):
	 	print("__delattr__")
	 	return super().__delattr__(name)

c = C()
c.x
c.x = 1
del c.x
c.x


print("----------------------------------------")
# we can use __get__, __set__, __delete__ to impelement property()
class MyDescriptor:
	def __get__(self, instance, owner):
		print("getting...", "MyDescriptor object is ", self, " the instance is ", instance, " the owner is", owner)

	def __set__(self, instance, value):
		print("setting...", self, instance, value)
	def __delete__(self, instance):
		print("deleting...", self, instance)

class Test:
	x = MyDescriptor()

test = Test()
test.x = 10
test.x
print("test is ", test)
del test.x



print("----------------------------------------")

class Celsius():
	def __init__(self, value = 28.0):
		self.value = value
	def __get__(self, instance, owner):
		return self.value
	def __set__(self, instance, value):
		self.value = float(value)

class Fahrenheit():
	def __get__(self, instance, owner):
		return instance.cel * 1.8 + 32
	def __set__(self, instance, value):
		instance.cel = (float(value) - 32) / 1.8

class Temperature:
	cel = Celsius()
	fah = Fahrenheit()

t = Temperature()
print(t.cel)
print(t.fah)
t.fah = 100
print(t.cel)
print(t.fah)
