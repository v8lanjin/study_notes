## 使用Eclipse 来Debug Android C/C++代码

1. 安装 Eclipse CDT， 假设放在`~/bin/eclipse-cpp/eclipse`
1. 安装Cross Compiler 的 gdb， `aarch64-linux-gnu-`
1. 进入Android AOSP目录，`. build/envsetup.sh && lunch xxx-eng` 建立android编译环境
1. 在AOSP目录下运行eclipse`~/bin/eclipse-cpp/eclipse`
1. 将workspace设置到AOSP目录上
1. 点击Debug configuration -> c/c++ remote application创建新的debug选项
1. 右边在main Tab中 c/c++ application选择我们编译出来的在symbol中的可执行文件`$OUT/symbols/system/bin/xxx`
1. 点击最下面一行的 select other, 勾选use configuration specific settings，然后勾选下面的GDB(DSF)Manual remote debugging launcher, 返回到上一级界面后选择，disable auto build
1. 点击Debugger Tab, 将gdb debugger设置为我们的/path/to/aarch64-linux-gnu-gdb, GDB command file 指定到`~/.gdbinit`
1. 点击Debugger Tab中的Connection Tab，将port设置为5039
1. 此时就可以debug了
1. 在debug的界面中我们添加一个debug console，来输入gdb命令`window->show view->debugger console`