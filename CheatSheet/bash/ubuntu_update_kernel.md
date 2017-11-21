### 下载编译 Ubuntu的kernel并使用新的kernel

1. 下载工具：  
```
sudo apt-get install dpkg-dev
sudo apt-get build-dep linux-image-$(uname -r)

```

1. 下载源码：
``` apt-get source linux-image-$(uname -r) ```

1. 编译代码：
```
cp /boot/config-xxxx-generic .config # 拷贝内核当前的配置文件
sudo make oldconfig # 在内核当前配置文件上做简单修改（一些不同于当前配置或没有的配置项）
sudo make -j8 # -j8参数可以加速编译，数字根据你自己电脑cpu的情况做出修改
```

1. 安装内核
```
sudo make modules_install # 安装内核模块
sudo make install # 安装内核：内核映像文件、内核符号表、内核配置文件、grub启动配置
```

1. 更新grub启动参数
