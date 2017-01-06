# 字符串索引print("s为字符串‘APPLE’")
s = 'APPLE'
print('第一个字符为')
print(s[0])
#支持负数索引
print('最后一个字符为')
print(s[-1])

print('==================================')
#使用for循环来来遍历字符串
print('现在使用for循环来遍历')
for c in s:
    print(c)

print("可以使用ord()来获取每一个字符的编码值")
print('比方说ord("a") = ' + str(ord('a')))



print('==================================')

print('现在介绍字符串切片')
print('我们可以使用s[x:y]来得到字符串s中从第x位到第y-1位的数据， 例如s = "0123456789" ')
s = '0123456789'
print('s[1:5] = ' + s[1:5]) 
print('s[:5] = ' + s[:5])
print('s[1:] = ' + s[1:])
print('s[1:-1] = ' + s[1:-1])
print('s[5:1] = ' + s[5:1])



print('==================================')
print("常用的字符串函数")
t = '89'
print('第一类： 测试函数')
print("s.endswith(t) :" + str(s.endswith(t)) )
print("s.startswith(t) :" + str(s.startswith(t)) )
print("s.isalnum() :" + str(s.isalnum()) )
print("s.isalpha() :" + str(s.isalpha()) )
print("s.isdecimal() :" + str(s.isdecimal()) )
print("s.isdigit() :" + str(s.isdigit()) )
print("s.isidentifier() :" + str(s.isidentifier()) )
print("s.islower() :" + str(s.islower()) )
print("s.isnumeric() :" + str(s.isnumeric()) )
print("s.isprintable() :" + str(s.isprintable()) )
print("s.isspace() :" + str(s.isspace()) )
print("s.istitle() :" + str(s.istitle()) )
print("s.isupper() :" + str(s.isupper()) )
print("t in s  :" + str(t in s ) )

print('第二类搜索函数')
print("find 和 index 都可以得到字符串字串开始的位置例如")
print("s.index('567') " + str(s.index('567')))
print("s.find('567') " + str(s.find('567')))
print("区别在于当子串不存在时，index会报出异常ValueError，而find将会返回-1")
print("对应的还有rfind和rindex")

print("第三类：改变大小写")
print("s=heLLo World")
s="heLLo World"

print("s.capitalize() " + s.capitalize())
print("s.lower() " + s.lower())
print("s.upper() " + s.upper())
print("s.swapcase() " + s.swapcase())
print("s.titile() " + s.title())