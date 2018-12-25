# 如何下载Android AOSP

参考文档:  
https://mirrors.tuna.tsinghua.edu.cn/help/AOSP/  
https://www.jianshu.com/p/3922ec229077

1. 下载repo 脚本
    ```bash
    curl https://mirrors.tuna.tsinghua.edu.cn/git/git-repo > ~/bin/repo
    chmod a+x ~/bin/repo
    ```  
1. 设置下载源
    ```bash
    export REPO_URL='https://mirrors.tuna.tsinghua.edu.cn/git/git-repo/'
    ```  
1. 查找自己需要的android版本号， 可以从http://androidxref.com/上看到， 例如Pie - 9.0.0_r3。 具体详细的列表可以从google的官方网站找到

1. 按照版本号初始化
    ```bash
    mkdir aosp && cd aosp
    repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest -b android-9.0.0_r3
    ```
1. 下载相关代码
    ```bash
    #下载完整的aosp
    repo sync -j16
    #或者只下载自己感兴趣的部分
    repo sync platform/frameworks/base -j8
    ```

PS：  
1. 关于上面感兴趣的包的名称， 可以在初始化好的repo目录下找到， 具体为止在`.repo/manifest.xml`, 例如 `<project path="frameworks/base" name="platform/frameworks/base" groups="pdk-cw-fs,pdk-fs" />` 表示会从远端的`platform/frameworks/base`处把项目下载到本地的`frameworks/base`

1. 关于获取android版本号， 可以先建立一个临时文件夹，不加参数，初始化为最新的android，通过git tag来获取素有版本号
    ```bash
    repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest
    cd .repo/manifests.git
    git tag
    ```
