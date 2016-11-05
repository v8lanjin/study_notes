# Note for ["Linux GPU Driver Developer’s Guide"](https://01.org/linuxgraphics/gfx-docs/drm/gpu.html)

## driver 初始化
一般都会有一个 `struct drm_driver`， 通常驱动都会静态初始化该结构体，然后传给`drm_dev_alloc()` 来分配一个device的实例化对象。当该对象完全初始化之后，在通过`drm_dev_register()`将其注册。这样userspace就可以访问到他了

>总结：
>1. 创建并初始化drm_driver
>1. 用drm_dev_alloc()创建 device对象。
>1. 初始化完device对象后，用drm_dev_register()完成注册（此后usermode就可以访问了）

### Driver Information
`struct drm_driver`包含：1. 一些静态属性，2. 一些DRM定义的接口实现
静态属性用于描述：支持的特性
方法用于实现：DRM api定义的操作
