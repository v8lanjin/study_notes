## 如何在Android中打印出java的调用栈：

1. 一般可以通过  
```Log.v(TAG,"Backtrace info:" , new Exception());```
1. 或者  
```Log.v(TAG, Log.getStackTraceString(new Exception()));```



## Android Studio 添加系统签名：
1. 首先需要一个下载好一个android aosp 以便获取签名需要的文件， 需要的文件在 build/target/product/security/ 需要的文件有platform.x509.pem、platform.pk8
1. 下载keytool-importkeypair工具：  
```git clone https://github.com/getfatday/keytool-importkeypair.git```
1. 生成证书文件  
```./keytool-importkeypair -k demo.jks -p 123456 -pk8 platform.pk8 -cert platform.x509.pem -alias demo```
1. 配置build.gradle  
在project里的有两个build.gradle, 这里需要修改的是project下app文件夹里的build.gradle,添加下面的内容
    ```
    +    signingConfigs {
    +        release {
    +            storeFile file('~/android-studio/keytool-importkeypair/demo.jks')
    +            storePassword '123456'
    +            keyAlias 'demo'
    +            keyPassword '123456'
    +        }
    +        debug {
    +            storeFile file("~/android-studio/keytool-importkeypair/demo.jks")
    +            storePassword '123456'
    +            keyAlias 'demo'
    +            keyPassword '123456'
    +        }
    +    }
        buildTypes {
            release {
                minifyEnabled false
                proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
    +            signingConfig signingConfigs.release
            }
        }
    ```
1. 编写程序，添加系统权限申请  
打开Android.mk 在 package节点下添加
    ```
    android:sharedUserId="android.uid.system"
    ```

