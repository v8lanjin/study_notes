## 安装postgresql与pgadmin3

sudo apt-get install postgresql-9.6
sudo apt-get install pgadmin3

1. 修改postgres用户的密码
```shell
sudo -u postgres psql
postgres=> alter user postgres password '新的密码';
```
开启postgresql服务
```shell
sudo -u postgres -H /usr/lib/postgresql/9.6/bin/pg_ctl -D /var/lib/postgresql/9.6/main -l logfile
# 可能会遇到说logfile permission denied的问题，那个是因为无法在当前文件夹创建logfile文件
# 单独创建一个文件夹，并将他的所有者改为postgres，然后在这个文件夹下面执行上述命令即可

#但是该方法启动的sql我没使用成功
```

```shell
sudo systemctl restart postgresql.service
```
打开pgadmin3，并链接到服务器上  
点击连接  
数据库名称： 随便  
主机地址：  localhost  
端口号：    默认  
服务：      空  
维护数据库： 默认（postgres）  
用户名：    默认（postgres）  
密码：     刚刚在上面修改的密码  
其他都用默认即可  