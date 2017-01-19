### 使用adb来设置设备休眠时间
```bash
#获取当前亮屏时间
adb shell settings get system screen_off_timeout
#设置休眠等待时间
adb shell settings put system screen_off_timeout 60
```
setting是android4.2（SDK17）加入的命令，具体可用值可以从[Settings](http://developer.android.com/reference/android/provider/Settings.System.html)处查看

### Logcat 相关参数
参考文章：  
[Ubuntu 下 使用 adb logcat 显示 Android 日志](http://www.hanshuliang.com/?post=32)  
[ Android的logcat命令详解](http://blog.csdn.net/mayingcai1987/article/details/6364657)  
保存日志输出到文件：
```
adb logcat -f 文件名
```
非阻塞输出log:
```
adb logcat -d
```
只输出某个TAG:
```
adb logcat -s TAG名称
```
显示某一级别及以上的信息：
```
adb logcat *:级别
```
显示某个TAG里某一级别及以上的信息：
```
adb logcat TAG名称:级别 *:S
```
