# 创建磁盘文件

```bash
mkdir -p rootfs_tmp
dd if=/dev/zero of=rootfs.ext4 bs=1024 count=131072
sudo mkfs.ext4 rootfs.ext4
sudo mount -o loop rootfs.ext4 ./rootfs_tmp

# 使用seek, 跳过seek个bs大小的块不写, 下面这条命令可以创建一个1G的文件,但是本身不占用磁盘空间(Linux支持稀疏文件)
dd if=/dev/zero of=fs.img bs=1M seek=1000 count=0
```