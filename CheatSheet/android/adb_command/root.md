## adb shell获取root权限

只针对自己编译的android，或者说原本shell是有root权限的，但是adb shell登陆之后发现只有shell权限

1. 直接在adb 的shell中输入su，看是否能够获得root权限
1. 执行如果提示permission denied, 查看在磁盘中su是否具有4777的权限
1. 执行如果提示setgid失败，查看su的所属用户是不是root

如果经过上述步骤可以获得一个root的shell，但是退出后再次登陆又变成了shell用户
可以查看/default.prop中的环境变量,如果```ro.secure=1```将他改为0
```bash
ro.secure=0
```

