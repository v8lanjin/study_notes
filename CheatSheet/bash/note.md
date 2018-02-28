1. 输出一个带格式的字符串  
shell中有命令printf，使用方法类似于C中的printf，例如我们要输出一个长度为5的数字，不足的部分用0来补齐
    ``` shell
    printf “%05d” 10
    ```
    如果需要赋值，可以使用var=$(printf xxxxx)的方式来实现

1. 动态输出文件内容：  
可以使用tail命令
    ```bash
    tail -F "文件名"
    ```

1. bash脚本中获取文件名或者路径  
参考链接：http://blog.csdn.net/ljianhui/article/details/43128465
    ```bash
    var=/dir/file.txt
    echo ${var##*/}
    file.txt

    echo ${var%/*}
    /dir
    ```

1. $参数  
[参考链接](https://www.cnblogs.com/chjbbs/p/6393805.html)
    ```bash
    echo $$ # 当前进程id
    echo $0 #当前脚本名
    echo $n #参数。第一个参数是$1，第二个参数是$2 。。。
    echo $# #参数个数
    echo $* #所有参数
    echo $@ #所有参数， 被双引号(" ")包含时，与 $* 稍有不同
    echo $? #返回值
    ```