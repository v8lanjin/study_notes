### Vim 分屏操作

1. 水平分屏 ```:sp```
1. 垂直分屏 ```:vsp```
1. 改变屏幕水平大小 ```ctrl+w <> 或者 ctrl+w n<> n代表移动n个char```
1. 改变屏幕垂直大小 ```ctrl+w -+= 或者 ctrl+w n-+```
1. 跳转到别的窗口   ```ctrl+w hjkl```

### NERD tree  
参考连接：
https://www.jianshu.com/p/eXMxGx
1. 开启快捷键 F10 主要看.vimrc里的配置``` map <F10> :NERDTreeToggle<CR> ```
1. ctrl + w + h    光标 focus 左侧树形目录
1. ctrl + w + l    光标 focus 右侧文件显示窗口
1. ctrl + w + w    光标自动在左右侧窗口切换 #！！！
1. ctrl + w + r    移动当前窗口的布局位置

### NERD commenter
参考链接  
http://blog.sina.com.cn/s/blog_4a033b09010107pf.html  
http://blog.sina.com.cn/s/blog_4a033b09010107p9.html  
Normal或者Visual 模式下：(\ 是leader键)
1. \ca，在可选的注释方式之间切换，比如C/C++ 的块注释和行注释//
1. \cc，注释当前行
1. \c，切换注释/非注释状态
1. \cs，以”性感”的方式注释
1. \cA，在当前行尾添加注释符，并进入Insert模式
1. \cu，取消注释
1. Normal模式下，几乎所有命令前面都可以指定行数
1. Visual模式下执行命令，会对选中的特定区块进行注释/反注释
