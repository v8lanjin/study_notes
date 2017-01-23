### aufs
aufs可以讲多个文件夹mount到一个结点上
例如可以讲文件夹changes以可写的方式，android以只读的方式挂在到文件夹target上  
这样，当我们在target文件夹内修改文件后，android不会收到影响，修改的内容会存在changes文件夹中  

``` bash
cd /tmp
mkdir changes android target
mount -t aufs -o dirs=./changes=rw:./android=ro none ./target
```
参考文章:  
[DOCKER基础技术:AUFS](http://coolshell.cn/articles/17061.html)
