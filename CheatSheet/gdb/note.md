### 1. 在gdb中打印完整的字符串

``` c
//会在gdb当前窗口输出
(gdb) printf "%s", x

//会在被debug的进程所处的窗口输出
(gdb) call printf("%s", x)
```
