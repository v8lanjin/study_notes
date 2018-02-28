### Tmux的常用命令
参考链接:  
[tmux shortcuts & cheatsheet](https://gist.github.com/MohamedAlaa/2961058)  
[十分钟学会tmux](http://www.cnblogs.com/kaiye/p/6275207.html)
[Linux进阶01：tmux](https://higoge.github.io/2015/07/20/ad-linux01/)
[优雅地使用命令行：Tmux 终端复用](http://harttle.com/2015/11/06/tmux-startup.htmlU)
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
1. 关闭当前分屏 `x`
1. 最大化/恢复当前pane  `z`
1. 将当前分屏前后移动 `{ or }`


#### 复制粘帖
1. 复制 `[`
1. 粘帖 `]`
1. 也可以 按住 `shift` 然后用鼠标拖动来复制，然后用`shift + insert`来粘贴

#### 有时候错误的复制了很多文字后然后粘帖之后会发现tmux下面有乱码
应该是粘帖的内容包含让tmux修改当前窗口名称的操作，导致名称被修改为超长的内容
解决方法：重新命名有问题的窗口
ctrl + prefix ","  ctrl+u
[参考链接](https://unix.stackexchange.com/questions/49886/tmux-status-bar-corrupted-after-catting-a-binary-file-how-to-reset)


####tmux打开很久之后，有时会发现鼠标滚轮会在tmux输入乱码
这个是Mouse-utf-8造成的，关闭即可
`set -g mouse-utf8 off`
`tmux set mouse-utf8 off`
[参考链接](https://superuser.com/questions/417027/why-are-random-characters-inserted-into-my-tmux-session)


当前使用的```.tmux.conf```


```
# act like GNU screen
#unbind C-b
#set -g prefix C-a
# improve colors
set -g default-terminal 'screen-256color'
#set -g default-terminal 'linux'
# act like vim
setw -g mode-keys vi
#bind h select-pane -L
#bind j select-pane -D
#bind k select-pane -U
#bind l select-pane -R
#bind-key -r C-h select-window -t :-
#bind-key -r C-l select-window -t :+
# 重新调整窗格的大小
bind K resizep -U 5
bind J resizep -D 5
bind-key L switch-client -l
#bind-key -n L switch-client -l
#开启window事件提示
setw -g monitor-activity on
#set -g visual-activity on
## 鼠标设置，不要打开，不然用鼠标选择不了内容
set -g mouse-utf8 on
set -g mouse on
#setw -g mode-mouse off
#set -g mouse-select-pane off
#set -g mouse-resize-pane off
#set -g mouse-select-window off
# start window numbers at 1 to match keyboard order with tmux window order
set -g base-index 1
set-window-option -g pane-base-index 1
# remove administrative debris (session name, hostname, time) in status bar
#set -g status-left ''
#set -g status-right ''
# increase scrollback lines
set -g history-limit 10000
# switch to last pane
bind-key C-a last-pane
# bind a reload key
bind R source-file ~/.tmux.conf \; display-message "Config reloaded.."
##### 状态栏设置
# colors
# soften status bar color from harsh green to light gray
set -g status-bg black
set -g status-fg white
# 状态栏中的窗口列表居中
set -g status-justify centre
# 状态栏启用utf-8
set -g status-utf8 on
#设置窗口列表颜色
#setw -g window-status-fg cyan
#setw -g window-status-bg default
#setw -g window-status-attr dim
#设置当前窗口在status bar中的颜色
setw -g window-status-current-fg white
setw -g window-status-current-bg red
setw -g window-status-current-attr bright
# spot at left
set-option -g status-left '#[bg=black,fg=green][#[fg=cyan]#S#[fg=green]]'
set-option -g status-left-length 20
# window list
setw -g automatic-rename on
#set-window-option -g window-status-format '#[dim]#I:#[default]#W#[fg=grey,dim]'
#set-window-option -g window-status-current-format '#[fg=cyan,bold]#I#[fg=blue]:#[fg=cyan]#W#[fg=dim]'
# spot at right
set -g status-right '#[fg=green][#[fg=cyan]%Y-%m-%d#[fg=green]]'

set -g prefix 'C-\'

set-window-option -g  xterm-keys on
```
