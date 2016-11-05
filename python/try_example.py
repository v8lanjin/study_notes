try:
	f = open('hello.txt')
	print(f.read())
	f.close()
except IOError as reason:
	print("File access Error")
	print(reason)



try:
	f = open('hello.txt')
	print(f.read())
	f.close()
except (IOError, TypeError):
	print("Find Error")



try:
	f = open('hello.txt')
	print(f.read())
except IOError as reason:
	print("File access Error")
	print(reason)
finally:
	try:
		f.close()
	except:
		print("do nothing")
	finally:
		print("file is closed")

try:
	raise
except :
	print("Error happened")
