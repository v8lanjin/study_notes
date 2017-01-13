### 使用adb来设置设备休眠时间
```bash
#获取当前亮屏时间
adb shell settings get system screen_off_timeout
#设置休眠等待时间
adb shell settings put system screen_off_timeout 60
```
setting是android4.2（SDK17）加入的命令，具体可用值可以从[Settings](http://developer.android.com/reference/android/provider/Settings.System.html)处查看
