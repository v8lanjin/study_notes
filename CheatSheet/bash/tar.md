## 使用tar来整合脚本与压缩包实现打包发布功能
参考链接：
1. <http://blog.csdn.net/jingxia2008/article/details/48730299>
1. <https://github.com/ruier/release_shell_scrtpts/blob/master/self_extract.sh>

使用tar的```-r, --append```参数可以实现将一个压缩包追加到脚本后面
从而可以在脚本中将后面的压缩包解压出来，并将解压的内容放置到合适的位置

```bash
tar -rf script.sh  append_file.tar.gz

```

```bash
#script.sh关键代码，假设脚本有9行，追加的文件就会从第十行开始
tail -n +10 $0 | tar zxv
exit 0

```
