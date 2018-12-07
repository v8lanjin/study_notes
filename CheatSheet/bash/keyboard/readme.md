# ubuntu下对键盘改建

参考链接: [如何不优雅的使用RK61机械键盘](http://there-is-no.info/how-to-hack-rk61-keyboard/)

### **由于上述文章地址已经失效, 搜索网页快照后, 摘录如下**

原文地址: http://there-is-no.info/how-to-hack-rk61-keyboard/

-----------------------
# 如何不优雅地使用RK61机械键盘

前一阵子闲着蛋疼在某宝入了RK61机械键盘，不像很多60键键盘，RK61的组合键丰富程度差到超乎想象，——只有F1～F12是有组合键映射的，像什么方向键啊，编辑键啊，都是没有的。v

最初我买这个键盘的时候就是本着软件映射解决一切的思想，结果却发现似乎那些组合键们是不好映射的。

但是试了好久才终于有办法去映射一些组合键了。

最早尝试过autohotkey的不正确的用法，linux里面用autokey。

两者的缺点就是，你可以很容易的把某种带有modifier的组合键映射成单键，但是再加入其他组合键的时候就SB了，比如，Shift+Left之类的，我写过一个脚本，生成了四十几组组合键，但是感觉这样实在是不优雅（作为一个键盘，使用软件映射似乎本来就不很优雅）。

还有一个问题就是不管使用Shift，Win，Alt作为修饰符（既然Fn键对操作系统是透明的，捕捉不到），都怕有一天真的用到了，以及可能触发一些系统的快捷键，软件来不及拦截。

后来读了好多autohotkey的文档，发现autohotkey是可以实习更底层的按键映射和条件按键映射的，作为“条件”，我第一个想到的就是牺牲Caps Lock键

Windows系统里这个问题是比较容易解决的，因为后来找到了autohotkey的按键映射和条件性的按键映射，最后就能得到一个这样的脚本：
```bash
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetCapslockState AlwaysOff
#If GetKeyState("Capslock", "P")
j::Left
k::Down
l::Right
i::Up
q::Ins
w::Home
e::PgUp
a::Del
s::End
d::PgDn
```
大意就是CapsLock始终是关闭的，按住CapsLock的时候就换到另一套按键映射。

搞定了Windows，有什么相同的办法搞定Linux吗？我没有找到。

~~直到那天看到了AltGr，还有xmodmap，AltGr是一个已经废弃了的修饰符，同时xmodmap这种X的比较底层的按键映射工具可以映射带AltGr的组合键，不过AltGr在那种情况下叫做Mode_switch，但是Ubuntu的xmodmap加载配置文件会导致X卡死，最后只能是写了一个shell脚本：~~

```bash
<del>xmodmap -e "keycode  66 = Mode_switch NoSymbol NoSymbol"
xmodmap -e "keycode  31 = i I Up"
xmodmap -e "keycode  44 = j J Left"
xmodmap -e "keycode  45 = k K Down"
xmodmap -e "keycode  46 = l L Right"
xmodmap -e "keycode  24 = q Q Insert"
xmodmap -e "keycode  25 = w W Home"
xmodmap -e "keycode  26 = e E Page_Up"
xmodmap -e "keycode  38 = a A Delete"
xmodmap -e "keycode  39 = s S End"
xmodmap -e "keycode  40 = d D Page_Down"</del>
```
~~可以插入到X的启动脚本里面，然后就是实现CapsLock的组合键映射到对应功能。~~

~~至于原本的keycode怎么看？可以用xmodmap -pke倒出来，然后看看是哪个字母就可以了。~~

上面xmodmap是有问题的，在Java的图形程序中是没法用的，后来有大神提出了linux里面用xkb的overlay做映射的方案，大致流程是这样的：

先建立一个按键符号表，不妨设为<your_favorite_path>/symbols/<your_favorite_symbol_file_name>，内容如下：
```bash
partial alphanumeric_keys
xkb_symbols "overlay"{
    key <AD08> {
        overlay1= <UP>
    };
    key <AC07> {
        overlay1= <LEFT>
    };
    key <AC08> {
        overlay1= <DOWN>
    };
    key <AC09> {
        overlay1= <RGHT>
    };
    key <AD01> {
        overlay1= <INS>
    };
    key <AD02> {
        overlay1= <HOME>
    };
    key <AD03> {
        overlay1= <PGUP>
    };
    key <AC01> {
        overlay1= <DELE>
    };
    key <AC02> {
        overlay1= <END>
    };
    key <AC03> {
        overlay1= <PGDN>
    };

    key <CAPS> {
        [ Overlay1_Enable ]
    };
};
```

每一个A_XX 是一个按键的位置，zxcv那一行是AB，然后z就是AB01，x就是AB02，asd那一行是AC，qwe那一行是AD，以此类推。

这样我们可以定义一个映射表。

之后，默认情况下overlay是锁定式的，就是说，你按了对应Overlay1_Enable的按键之后，所有按键按照他们overlay1的行为执行，就是说Q对应到了Insert，但这样可能不是很方便，所以要改一下overlay的行为，xkb通过兼容性设置定义这种行为，配置文件不妨设为<your_favorite_path>/compat/<your_favorite_compat_file_name>：
```bash
partial xkb_compatibility "overlay"{
    interpret Overlay1_Enable+AnyOfOrNone(all) {
          action= SetControls(controls=Overlay1);
    };
};
```
最后建立一个整体的xkb的配置，配置文件不妨设为<your_favorite_path>/keymap/<your_favorite_keymap_file_name>，内容大致如下：
```bash
xkb_keymap {
        xkb_keycodes  { include "evdev+aliases(qwerty)" };
        xkb_types     { include "complete"      };
        xkb_compat    { include "complete+<your_favorite_compat_file_name>"      };
        xkb_symbols   { include "pc+us+inet(evdev)+<your_favorite_symbol_file_name>"     };
        xkb_geometry  { include "pc(pc105)"     };
};
```
注意两处+号，其他部分可以通过setxkbmap -print得到。

之后通过xkbcomp应用keymap：
```bash
xkbcomp -I<your_favorite_path> <your_favorite_path>/keymap/<your_favorite_keymap_file_name> $DISPLAY
```
如果想获得完整的xkb配置文件参照，你可以用xkbcomp $DISPLAY output.xkb查看。