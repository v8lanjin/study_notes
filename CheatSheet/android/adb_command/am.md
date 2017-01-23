### 命令 am 的相关用法：

参考文献：  
[Am命令用法](http://gityuan.com/2016/02/27/am-command/)  


常用命令：
打开一个Activity：
```
am start -n package_name/.Acitivity_Name
#还有一个参数 -S，可以在启动activity之前，调用forceStopPackage()方法强制停止app.
```

```
#关闭一个app
adb shell am force-stop package_name
```
