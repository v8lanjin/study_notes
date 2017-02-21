### Tmux的常用命令
参考链接:  
[tmux shortcuts & cheatsheet](https://gist.github.com/MohamedAlaa/2961058)  
#### Session  
1. 新建一个session，并设定名称
```
tmux new -s Session_Name
```
1. attach到一个Session上
```
tmux a
```
1. attach 到某个Session上
```
tmux a -t Session_Name
```
1. list 所有Session
```
tmux ls
```
1. 切换到其他session
```
#进入session之后
ctrl+a s
```

#### 分屏  
1. 水平分屏 `"`
1. 垂直分屏 `%`
1. 最大化/恢复当前pane  `z`
