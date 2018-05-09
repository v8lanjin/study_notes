# 当/boot分区空间不足 删除无用的kernel

```shell
# 列出所有已经安装了的kernel
dpkg --get-selections|grep linux
#结果中 标记为install的就是已经安装了的

# 查看当前使用的版本号
uname -a

# 选择不需要的删除掉
sudo apt-get remove linux-image-xxxxxxxx
```