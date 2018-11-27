## vscode debug

首先编译出可以debug的bin文件

``` bash
gcc ***.c ***.c -g -o a.out
```

配置vscode的debug launch.json

```json
{
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
                {
                        "name": "(gdb) Launch",
                        "type": "cppdbg",
                        "request": "launch",
                        "program": "${workspaceFolder}/a.out",
                        "args": [],
                        "stopAtEntry": false,
                        "cwd": "${workspaceFolder}",
                        "environment": [],
                        "externalConsole": true,
                        "MIMode": "gdb",
                        "setupCommands": [
                                {
                                        "description": "Enable pretty-printing for gdb",
                                        "text": "-enable-pretty-printing",
                                        "ignoreFailures": true
                                }
                        ]
                }
        ]
}
```



## 在debug前添加编译功能

创建一个task.json `ctrl + shift + p` 输入 `configure task`

```json
{
        // See https://go.microsoft.com/fwlink/?LinkId=733558
        // for the documentation about the tasks.json format
        "version": "2.0.0",
        "tasks": [
                {
                        "label": "build test",
                        "type": "shell",
                        "command": "gcc",
                        "args": [
                                // Ask msbuild to generate full paths for file names.
                                "xxx.c",
                                "yyy.c",
                                "-o",
                                "a.out",
                                "-lm",
                                "-g"
                        ],
                        "group": "build",
                        "presentation": {
                                // Reveal the output only if unrecognized errors occur.
                                "reveal": "silent"
                        },
                        // Use the standard MS compiler pattern to detect errors, warnings and infos
                        "problemMatcher": "$msCompile"
                }
        ]
}
```

配置launch.json

```json
{
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
                {
                        "name": "(gdb) Launch",
                        "type": "cppdbg",
                        "request": "launch",
                        "program": "${workspaceFolder}/a.out",
                        "args": [],
                        "stopAtEntry": false,
                        "cwd": "${workspaceFolder}",
                        "environment": [],
                        "externalConsole": true,
                        "MIMode": "gdb",
                        "setupCommands": [
                                {
                                        "description": "Enable pretty-printing for gdb",
                                        "text": "-enable-pretty-printing",
                                        "ignoreFailures": true
                                }
                        ],
                        "preLaunchTask": "build test"
                }
        ]
}
```

*注意, launch中添加了一个preLaunchTask, 名字需要和task.json中的label相同*

