## 如何在Android中打印出java的调用栈：

1. 一般可以通过  
```Log.v(TAG,"Backtrace info:" , new Exception());```
1. 或者  
```Log.v(TAG, Log.getStackTraceString(new Exception()));```
