## 更换系统内核kernel

#### 参考链接
[How to Compile and Install Linux Kernel v4.9.11 Source On a Debian / Ubuntu Linux](https://www.cyberciti.biz/faq/debian-ubuntu-building-installing-a-custom-linux-kernel/)


1. 下载代码：
    ```bash
    sudo apt-get install linux-source-4.9
    #代码会被保存在/usr/src/linux-source-4.9.tar.xz
    #将他解压到合适的目录
    mkdir ~/code/linux-kernel -p
    cd ~/code/linux-kernel
    tar xvf /usr/src/linux-source-4.9.tar.xz
    ```

1. 编译内核
    ```bash
    #0. 清理
    make distclean
    make-kpkg clean

    #1. 获得config文件
    cp -v /boot/config-$(uname -r) .config
    make menuconfig

    #2. 编译kernel
    fakeroot make-kpkg --initrd --revision=1.0.NAS kernel_image kernel_headers -j16

1. 安装kernel
    ```bash
    #编译完成后在上层目录会生成两个deb文件
    #../linux-headers-xxxx_amd64.deb
    #../linux-image-xxxx_amd64.deb
    cd ../
    sudo dpkg -i linux-image-xxxx_amd64.deb
    sudo dpkg -i linux-headers-xxxx_amd64.deb
    ```
1. 重启系统,通过uname命令查看内核是否更新