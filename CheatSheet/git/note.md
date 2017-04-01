### 系统用户名与git版本库里用户名不一样时ssh key如何指定

在开发过程中经常遇到系统当前用户名和git版本库里的用户名不匹配的情况
例如：在系统里的用户名为"user1", 在github上的帐号名叫"user2"
那么在git clone时可以加上自己的在git repo中的用户名
```
git clone ssh://user2@xxxxxxx
```
如果不想显示指定用户名那么可以当前用户的~/.ssh/config中进行配置

```
# Default github user(first@mail.com)                                                                                                                                                                    
 Host *.github.com                                                                                                                                                                                
 User user2                                                                                                                                                                                  
 IdentityFile ~/.ssh/id_rsa 
```
这样在配置之后，当git clone github.com上的内容时会自动使用user2来下载
