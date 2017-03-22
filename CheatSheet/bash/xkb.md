### 使用xkb来修改键盘映射

XKB可以用于修改Ubuntu图形界面下的键盘映射
可以通过修改/usr/share/X11/xkb/symbols/中的us和pc
修改完成后需要注销重新登陆起效

也可以通过如下命令临时修改
```bash
xkbcomp $DISPLAY output.xkb #得到当前的xkb键盘配置
#修改output.xkb 文件
xkbcomp output.xkb $DISPLAY #使配置生效
```
我的修改：  
+ CAPS Lock -> modifier 
+ hjkl -> 左下上边
+ u/i -> home/end
+ q -> shift
+ 右ctrl -> caps lock

```
$ diff -Naur pc-bak pc
--- pc-bak	2017-03-03 20:36:07.052040180 +0800
+++ pc	2017-03-10 21:32:38.456866386 +0800
@@ -19,7 +19,7 @@
     key  <TAB> {	[ Tab,	ISO_Left_Tab	]	};
     key <RTRN> {	[ Return		]	};
 
-    key <CAPS> {	[ Caps_Lock		]	};
+    key <CAPS> {	[ Mode_switch	]	};
     key <NMLK> {	[ Num_Lock 		]	};
 
     key <LFSH> {	[ Shift_L		]	};
@@ -27,14 +27,14 @@
     key <LWIN> {	[ Super_L		]	};
 
     key <RTSH> {	[ Shift_R		]	};
-    key <RCTL> {	[ Control_R		]	};
+    key <RCTL> {	[ Caps_Lock		]	};
     key <RWIN> {	[ Super_R		]	};
     key <MENU> {	[ Menu			]	};
 
     // Beginning of modifier mappings.
     modifier_map Shift  { Shift_L, Shift_R };
-    modifier_map Lock   { Caps_Lock };
-    modifier_map Control{ Control_L, Control_R };
+    modifier_map Lock   { Control_R };
+    modifier_map Control{ Control_L };
     modifier_map Mod2   { Num_Lock };
     modifier_map Mod4   { Super_L, Super_R };
```
```
--- us-bak	2017-03-03 20:36:18.676206011 +0800
+++ us	2017-03-10 22:05:42.480942045 +0800
@@ -17,14 +17,14 @@
     key <AE11> {	[     minus,	underscore	]	};
     key <AE12> {	[     equal,	plus		]	};
 
-    key <AD01> {	[	  q,	Q 		]	};
-    key <AD02> {	[	  w,	W		]	};
-    key <AD03> {	[	  e,	E		]	};
-    key <AD04> {	[	  r,	R		]	};
-    key <AD05> {	[	  t,	T		]	};
+    key <AD01> {	[	  q,	Q 		], [ Shift_L ]	};
+    key <AD02> {	[	  w,	W		], [ Control_L ] };
+    key <AD03> {	[	  e,	E		]   };
+    key <AD04> {	[	  r,	R		]   };
+    key <AD05> {	[	  t,	T		]   };
     key <AD06> {	[	  y,	Y		]	};
-    key <AD07> {	[	  u,	U		]	};
-    key <AD08> {	[	  i,	I		]	};
+    key <AD07> {	[	  u,	U		], [ Home ]	};
+    key <AD08> {	[	  i,	I		], [ End  ]	};
     key <AD09> {	[	  o,	O		]	};
     key <AD10> {	[	  p,	P		]	};
     key <AD11> {	[ bracketleft,	braceleft	]	};
@@ -35,10 +35,10 @@
     key <AC03> {	[	  d,	D		]	};
     key <AC04> {	[	  f,	F		]	};
     key <AC05> {	[	  g,	G		]	};
-    key <AC06> {	[	  h,	H		]	};
-    key <AC07> {	[	  j,	J		]	};
-    key <AC08> {	[	  k,	K		]	};
-    key <AC09> {	[	  l,	L		]	};
+    key <AC06> {	[	  h,	H		], [ Left ]	};
+    key <AC07> {	[	  j,	J		], [ Down ]	};
+    key <AC08> {	[	  k,	K		], [ Up   ]	};
+    key <AC09> {	[	  l,	L		], [ Right ]	};
     key <AC10> {	[ semicolon,	colon		]	};
     key <AC11> {	[ apostrophe,	quotedbl	]	};
```

参考链接：
 
1. <https://github.com/Chunlin-Li/Chunlin-Li.github.io/blob/master/blogs/linux/ubuntu-xkb-keyboard-remap.md>
1. <https://www.linux.com/learn/hacking-your-linux-keyboard-xkb>
1. <https://www.x.org/releases/X11R7.6/doc/xorg-docs/input/XKB-Config.html>
1. <https://wiki.archlinux.org/index.php/X_KeyBoard_extension>
1. <https://wiki.archlinux.org/index.php/Keyboard_configuration_in_Xorg>