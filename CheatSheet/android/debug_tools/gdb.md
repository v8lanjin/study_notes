### 使用CGDB来 Debug


##### 开发板端：

1. debug 具体文件 ``` gdbserver(64) :5039 /system/bin/xxx```
1. debug 某个进程：``` gdbserver(64) :5039 ??????```

##### PC端：

1. 首先安装CGDB ```sudo apt-get install cgdb```
1. 转发端口 ``` adb forward tcp:5039 tcp:5039 ```
1. 进入到Android 源码目录执行cgdb
```shell
cd $ANDROD_SEC
cgdb -d $path/to/gdb $OUT/symbol/system/bin/xxx
```
1. 进入cgdb的UI界面之后     
```shell
export AndroidDir="/path/to/android_aosp"
set solib-search-path $AndroidDir/out/target/product/juno/symbols/system/lib64:$AndroidDir/out/target/product/juno/symbols/system/vendor/lib64:$AndroidDir/out/target/product/juno/symbols/system/vendor/lib64/hw
set solib-absolute-prefix $AndroidDir/out/target/product/juno/symbols/
target remote :5039
```

参考链接：
1. <https://developer.android.com/studio/command-line/adb.html>