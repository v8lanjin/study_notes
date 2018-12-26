# 当/boot分区空间不足 删除无用的kernel
参考链接: https://blog.csdn.net/along_oneday/article/details/75148240
```shell
# 列出所有已经安装了的kernel
dpkg --get-selections|grep linux
#结果中
# 标记为install的就是已经安装了的
# 标记为 deinstall: 表示已经被remove, 但是没有被purge
# 标记为 purge:     表示已经被purge, 但是没有被remove

# 查看当前使用的版本号
uname -a

# 选择不需要的删除掉
sudo apt-get remove linux-image-xxxxxxxx
sudo dpkg -P linux-image-xxxx
sudo apt-get autoremove
```

# 删除不用的旧 kernel 内核

参考文章: [移除Ubuntu 16.04中旧版内核的几种方式](https://www.linuxidc.com/Linux/2016-05/131143.htm)

```
#方法1
sudo apt autoremove --purge
```


```
#方法2:
sudo apt install byobu
sudo purge-old-kernels
```


```
#方法3:
uname -r #当前使用的kernel
dpkg -l | tail -n +6| grep -E 'linux-image-[0-9]+'| grep -Fv $(uname -r) #列出所有kernel
sudo dpkg --purge linux-image-4.4.0-21-generic #移除不用的kernel
```
>rc：表示已经被移除  
>ii：表示符合移除条件（可移除）  
>iU：已进入 apt 安装队列，但还未被安装（不可移除）
