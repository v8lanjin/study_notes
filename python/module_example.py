
import generator_example as ge

print("==============================")
for each in ge.feb():
	if each > 100:
		break
	print(each)


print ("------------------------------")
from generator_example import feb # from x import y/*


for each in feb():
	if each > 100:
		break
	print(each)

print(__name__)

# if __name__ == '__main__'
import sys
print(sys.path)
#if you want, you can add search path into sys.path
# sys.path.append(xxxxxxx)

# creat a package
# step 1. create a dir, the name of dir is the name of package like Pack1
# step 2. create a __init__.py under the dir like touch Pack1/__init__.py
# step 3. create yyy.py under dir like Pack1/yyy.py and def func func1
# step 4. use the package like import Pack1.yyy as xx  and use it like xx.func1



# package related magic func __all__, __file__, __doc__ and dir()