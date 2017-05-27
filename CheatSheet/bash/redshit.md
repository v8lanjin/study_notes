###redshift使用
1. 单屏幕：
```
#!/bin/bash
# 保存为 redshift.sh
gamma=5000
if [[ $1 != "" ]];
then
    gamma=$1;
fi
redshift -l 23.0:120.6 -t 5500:4500 -g 0.9 -m vidmode -o -O $gamma
```


1. 双屏幕：

```
xrand #可以得到当前系统里面所有的显示器
Screen 0: minimum 320 x 200, current 3840 x 1200, maximum 8192 x 8192
VGA-1 connected primary 1920x1080+1920+0 (normal left inverted right x axis y axis) 509mm x 286mm
   1920x1080     60.00*+
   1600x1200     60.00  
   1680x1050     59.95  
   1600x900      60.00  
   1280x1024     75.02    60.02  
   1440x900      59.89  
   1280x800      59.81  
   1152x864      75.00  
   1024x768      75.03    70.07    60.00  
   832x624       74.55  
   800x600       72.19    75.00    60.32    56.25  
   640x480       75.00    72.81    66.67    59.94  
   720x400       70.08  
DP-1 connected 1920x1200+0+0 (normal left inverted right x axis y axis) 518mm x 324mm
   1920x1200     59.95*+
   1920x1080     60.00  
   1600x1200     60.00  
   1680x1050     59.95  
   1280x1024     60.02  
   1280x960      60.00  
   1024x768      60.00  
   800x600       60.32  
   640x480       59.94  
   720x400       70.08  
HDMI-1 disconnected (normal left inverted right x axis y axis)
DP-2 disconnected (normal left inverted right x axis y axis)
HDMI-2 disconnected (normal left inverted right x axis y axis)
DP-1-3 disconnected
DP-1-4 disconnected

sudo redshift -m randr:screen=DP-1 -t 5500:4000
```
