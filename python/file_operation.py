f = open("readme.txt", 'r')

print(f)

num = 0;
for eachLine in f:
	num = num + 1
	print(str(num) + ": " + eachLine)

f.seek(0, 0)

l = list(f)
print(l)
f.close()


f = open("write_test.txt", "w")
f.write("Hello World\n")
f.close()