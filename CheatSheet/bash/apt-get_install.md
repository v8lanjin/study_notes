# 安装指定版本的软件
1. 更新
    ```bash
    sudo apt-get update
    ```
1. 查找当前版本号
    ```bash
    apt-cache madison [软件名]
    #例如 apt-cache madison code; 查找vscode 所有版本号
    # apt-cache madison code
    #      code | 1.30.1-1545156774 |     https://packages.microsoft.com/repos/vscode     stable/main amd64 Packages
    #      code | 1.30.0-1544567151 |     https://packages.microsoft.com/repos/vscode     stable/main amd64 Packages
    #      code | 1.29.1-1542309157 |     https://packages.microsoft.com/repos/vscode     stable/main amd64 Packages
    # .................
    ```
1. 安装指定版本:
    ```bash
    sudo apt-get install [软件名=版本号]
    #例如: sudo apt-get install code=1.29.1-1542309157
    ```
