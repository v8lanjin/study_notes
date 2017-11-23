## 在windows上安装pygraphviz

### 方法一：
- PS. 因为64位的原因，导致无法正常安装pygraphviz经过搜索，最终成功编译出lib，并可以导入python中，但在是计划图中依旧遇到问题

1. 首先从官网下载安装graphviz
1. 然后下载第三方的64位[graphviz](https://github.com/mahkoCosmo/GraphViz_x64)
1. 将两个版本的graphviz的bin和lib都分别加入到系统环境变量中
1. 下载官方pygraphviz的源码
1. 添加[PyIOBase_Type error 的 patch](https://github.com/Kagami/pygraphviz/commit/fe442dc16accb629c3feaf157af75f67ccabbd6e)
1. 编辑pygraphviz源码setup.py，告诉他我们的graphviz的路径include_dirs 和 library_dirs
1. `python setup.py install`




### 方法二：
参考链接[Easy-Digraph-Draw](https://github.com/darkhipo/Easy-Digraph-Draw)

对于安装有Anaconda的环境来说

1. 正常安装 graphviz for win 以及[c++编译器](http://landinghub.visualstudio.com/visual-cpp-build-tools)
1. 将graphviz的bin和lib目录加入到系统的环境变量中

1. 现将整体工作环境切换到python3.4
    ```bash
    #创建py3.4工作环境
    conda create --name digraphs python=3.4 anaconda
    #切换到3.4的环境
    activate digraphs
    ```
1. 下载已经编译好的pygraphviz whl文件[pygraphviz‑1.3.1‑cp34‑none‑win_amd64.whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygraphviz)

1. 安装
    ```bash
    #在3.4的环境下
    pip install pygraphviz‑1.3.1‑cp34‑none‑win_amd64.whl
    ```
