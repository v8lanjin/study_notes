### Sublime Text 3 无法使用package control

参考链接： <http://www.jianshu.com/p/a3af44257b15>

进入控制台```ctrl + ` ``` 可以看到是获取http://packagecontrol.io/channel_v3.json超时
可以手工用浏览器或wget将该文件下载下来，然后用python启动一个简单的http服务
```bash
cd /tmp;
wget http://packagecontrol.io/channel_v3.json
python -m SimpleHTTPServer 8080
```
然后进入sublime，在preferences -> package settings -> package control -> setting user
加入
```
    "channels":
    [
        "http://localhost:8080/channel_v3.json"
    ],
```

