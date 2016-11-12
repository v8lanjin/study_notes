# generator_example.py
def myGen():
	print("Generator is running!")
	yield 1
	yield 2

if __name__ == "__main__":
	myG = myGen()
	print('---')
	print(next(myG))
	print('---')
	print(next(myG))
else:
	print(__name__)


def feb():
	a = 0
	b = 1
	while True:
		a, b = b, a + b
		yield a

# feb()
for each in feb():
	if each > 100:
		break
	print(each)