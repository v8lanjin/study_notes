# FileProvider


java.lang.Object
   ↳    android.content.ContentProvider
       ↳    android.support.v4.content.FileProvider

　　FileProvider是ContentProvider的子类，他让文件在在app中共享更加安全，他使用content://uri而不是file:///uri  

　　一个content uri允许你给一个临时文件访问赋予读写权限，当你构建了一个包含content的Intent对象来传递content uri
给客户端app时，你可以调用Intent.setFlags()来增加权限，客户端对文件的访问权限将持续有效只要接受该uri的activity
处于活动状态。 如果该intent是传递给service，那只要该service处于运行状态，那么该权限将持续有效

　　作为对比， 通过file:///uri来控制文件访问权限，完全依赖于文件自身的权限设置。文件的权限对所有的app都是一样有效的
一次从本质上来说是不安全的

　　FileProvider所提供的更安全的文件访问控制使得他成为了Android安全基础设施的重要组成部分

　　本文主要描述以下主题
1. 定义FileProvider
1. Specifying Available Files
1. Retrieving the Content URI for a File
1. 给一个uri赋予临时权限
1. Serving a Content URI to Another App

## 定义FileProvider
因为FileProvider的默认包含了生成Content URI的功能，一次你无需自己在代码中定义他的子类，相反你只需要在xml文件中
指明即可。 要指定FileProvider，你需要在你的manifest文件中添加一个`<provider>`元素，将`android:name`设置为
`android.support.v4.content.FileProvider`。设置`android:authorities`为一个基于你所能控制域的URI授权，例如如果
你所能控制的域为`mydomain.com`,你应该使用授权`com.mydomain.FileProvider`， 设置`android:exported`为false。
FileProvider不需要是public的。设置`android:grantUriPermissions`为true，这可以让你能够授予临时的文件访问权限
例如：
```xml
<manifest>
    ...
    <application>
        ...
        <provider
            android:name="android.support.v4.content.FileProvider"
            android:authorities="com.mydomain.fileprovider"
            android:exported="false"
            android:grantUriPermissions="true">
            ...
        </provider>
        ...
    </application>
</manifest>
```
如果你想覆写FileProvider的默认行为，那你需要创建一个子类，并在xml文件中给`<provider>`的anroid:name使用完整的类名

## Specifying Available Files
FileProvider只能为你提前制定的文件生成Content URI, 要制定一个目录，你需要子xml文件中通过`<paths>`的子类制定他的
存储区域以及路径。例如，下面的`paths`匀速告诉FileProvider你想要为你私有的文件域中的子文件夹images创建一个Content uri
```
<paths xmlns:android="http://schemas.android.com/apk/res/android">
    <files-path name="my_images" path="images/"/>
    ...
</paths>
```

`<paths>`元素必须至少包含一个如下的子元素
```
<files-path name="name" path="path" />
```
> 代表你app内部存储的`/files`下的文件，这个子文件夹和`Context.getFilesDir()`的结果一样  

```
<cache-path name="name" path="path" />
```
> 同上：内部存储的cache文件夹 = `getCahceDir()`  

```
<external-path name="name" path="path" />
```
> 同上：外部存储的根节点 = `Environment.getExternalStorageDirectory()`  

```
<external-files-path name="name" path="path" />
```
> 你app在外部存储中的根节点 = `Context#getExternalFilesDir(String) Context.getExternalFilesDir(null)`  
    
```
<external-cache-path name="name" path="path" />
```
> 表示你app自己在外部存储中的cache的根节点 = `Context.getExternalCacheDir()`


