### 搭建一个tftp server
参考链接：
<http://www.cnblogs.com/shenhaocn/archive/2011/03/13/1983042.html>

```bash
#安装
sudo apt-get install tftp-hpa tftpd-hpa

#创建共享路径
mkdir /tftpboot
sudo chmod 777 /tftpboot

#编辑配置文件
sudo gedit /etc/default/tftpd-hpa 
```
```
# /etc/default/tftpd-hpa

TFTP_USERNAME="tftp"
TFTP_DIRECTORY="/tftpboot"
TFTP_ADDRESS="[::]:69"
TFTP_OPTIONS="--secure -B 2000"

```
```bash
#重启tftp server
sudo service tftpd-hpa restart  
```

