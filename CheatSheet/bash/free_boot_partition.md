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