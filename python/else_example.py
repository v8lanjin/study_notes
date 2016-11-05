#else
# if :  else:
# for/while: else:  else content will be triggered once the loop is be processed completly, that means there is no 'break'
# try:  else:    if there is no except the else content will be triggered

try:
	int('abc')
except:
	print("sorry, there is something wrong")
else:
	print("good, there is no error")

print('==================')

try:
	int('123')
except:
	print("sorry, there is something wrong")
else:
	print("good, there is no error")

print('================')

# with command
# this command will help you close file automatically
# try:
# 	f = open('data.txt', 'r')
# 	for each_line in f:
# 		print(each_line)
# except IOError as reason:
# 	print("error: " + str(reason))
# finally:
# 	f.close()
try:
	with open('data.txt', 'r') as f:
		for each_line in f:
			print(each_line)
except IOError as reason:
	print(reason)
