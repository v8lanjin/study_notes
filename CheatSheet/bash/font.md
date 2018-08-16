# 使用 Source Code Pro 字体

参考连接:[在Ubuntu 中使用Source Code Pro字体] (https://blog.csdn.net/android_hasen/article/details/50523013)

1. 下载: https://github.com/adobe-fonts/source-code-pro/downloads
1. 解压, 并将其中的所有.otf文件拷贝到 ~/.fonts/ 文件夹下
1. 执行 fc-cache -f -v 命令
1. 在terminator中使用该字体, 我用的是Source Code Pro Semibold 大小为 11
1. 在vscode中使用该字体,
```
    "editor.cursorStyle": "line",
    "editor.fontFamily": "Source Code Pro",
    "editor.rulers": [90,120],
    "editor.fontSize": 18,
```

