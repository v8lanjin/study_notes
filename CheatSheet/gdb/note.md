### 1. 在gdb中打印完整的字符串

``` c
//会在gdb当前窗口输出
(gdb) printf "%s", x

//会在被debug的进程所处的窗口输出
(gdb) call printf("%s", x)

//输出数组
(gdb) p *array@len
```
### 1. 用watch命令检测一个内存地址的变化
首先通过p命令得到目标地址，然后可以通过
```
watch *(type*)addr
#例如
watch *(int*)0x12345678
```
