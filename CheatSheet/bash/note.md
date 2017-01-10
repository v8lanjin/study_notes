1. 输出一个带格式的字符串
shell中有命令printf，使用方法类似于C中的printf，例如我们要输出一个长度为5的数字，不足的部分
用0来补齐
``` shell
printf “%05d” 10
```
如果需要赋值，可以使用var=$(printf xxxxx)的方式来实现

1. 动态输出文件内容：
可以使用tail命令
``` shell
tail -F "文件名"
```
