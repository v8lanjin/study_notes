## Terminator 配置

### 1. 配色
1.1 背景色， 来自于sublime的背景色 #272822(39, 40, 34)  
1.2 调色盘： 来自于 [iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes) 中的[Monokai Soda](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/terminator/Monokai%20Soda.config)
```
#原始配色为
#1a1a1a:#f4005f:#98e024:#fa8419:#9d65ff:#f4005f:#58d1eb:#c4c5b5:#625e4c:#f4005f:#98e024:#e0d561:#9d65ff:#f4005f:#58d1eb:#f6f6ef

#我将其中黄色也修改为了橘黄色，结果为
#1a1a1a:#f4005f:#98e024:#fa8419:#9d65ff:#f4005f:#58d1eb:#c4c5b5:#625e4c:#f4005f:#98e024:#fa8419:#9d65ff:#f4005f:#58d1eb:#f6f6ef

```
1.3 背景透明，不透明度为91%


### 2. 快捷键
我多窗口切换的快捷键从`alt+上下左右` 修改为了`ctrl + hjkl`

### 3. 隐藏标题栏
取消选中 Preference->Profiles->Show titlebar

### Appendix:
我的配置文件`~/.config/terminator/config`
```
[global_config]
[keybindings]
  go_down = <Primary>j
  go_left = <Primary>h
  go_right = <Primary>l
  go_up = <Primary>k
[layouts]
  [[default]]
    [[[child1]]]
      parent = window0
      type = Terminal
    [[[window0]]]
      parent = ""
      type = Window
[plugins]
[profiles]
  [[default]]
    background_color = "#272822"
    background_darkness = 0.91
    background_image = None
    background_type = transparent
    foreground_color = "#c7c9c9"
    palette = "#1a1a1a:#f4005f:#98e024:#fa8419:#9d65ff:#f4005f:#58d1eb:#c4c5b5:#625e4c:#f4005f:#98e024:#fa8419:#9d65ff:#f4005f:#58d1eb:#f6f6ef"
    scrollback_infinite = True
    show_titlebar = False
    urgent_bell = True
    use_system_font = False
```