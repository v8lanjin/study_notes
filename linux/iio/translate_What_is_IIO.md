# What is IIO?

原文: https://iiobits.wordpress.com/2015/01/21/what-is-iio/

IIO是一个为模数/数模转换器或相关硬件服务的内核子系统, 由Jonathan Cameron 以及 linux-iio社区于2009年开发. 这一类设备有陀螺仪, 加速计, 光线传感器, 磁力传感器等等



IIO可以分为两层, 一个为devices, 一个为channels:

* device 处于最顶层, 代表这个芯片, 由 struct iio_info 和 struct iio_dev 表示
* channel 代表这个设备的一个捕获源, 用 struct iio_chan_spec 表示

IIO 设备 通过sysfs或者字符设备节点与用户交流

假如我们有一个3轴加速度计, mma8452. 加载驱动后, 我们将在` /sys/bus/iio/devices/iio:device0/ `下面看到如下信息

```bash
roberta@bazinga:~$ ls -l /sys/bus/iio/devices/iio:device0/
(...)
-rw-r--r-- 1 root root 4096 ian 21 17:01 in_accel_sampling_frequency
-rw-r--r-- 1 root root 4096 ian 21 17:01 in_accel_scale
-rw-r--r-- 1 root root 4096 ian 21 17:01 in_accel_x_calibbias
-rw-r--r-- 1 root root 4096 ian 21 17:01 in_accel_x_raw
-rw-r--r-- 1 root root 4096 ian 21 17:01 in_accel_y_calibbias
-rw-r--r-- 1 root root 4096 ian 21 17:01 in_accel_y_raw
-rw-r--r-- 1 root root 4096 ian 21 17:01 in_accel_z_calibbias
-rw-r--r-- 1 root root 4096 ian 21 17:01 in_accel_z_raw
(...) 
```

相关的channel定义代码如下

```c
#define MMA8452_CHANNEL(axis, idx) { \
    .type = IIO_ACCEL, \
    .modified = 1, \
    .channel2 = IIO_MOD_##axis, \
    .info_mask_separate = BIT(IIO_CHAN_INFO_RAW) | \
        BIT(IIO_CHAN_INFO_CALIBBIAS), \
    .info_mask_shared_by_type = BIT(IIO_CHAN_INFO_SAMP_FREQ) | \
        BIT(IIO_CHAN_INFO_SCALE), \
    .scan_index = idx, \
    .scan_type = { \
        .sign = 's', \
        .realbits = 12, \
        .storagebits = 16, \
        .shift = 4, \
        .endianness = IIO_BE, \
    }, \
}
static const struct iio_chan_spec mma8452_channels[] = {
    MMA8452_CHANNEL(X, 0),
    MMA8452_CHANNEL(Y, 1),
    MMA8452_CHANNEL(Z, 2),
    IIO_CHAN_SOFT_TIMESTAMP(3),
};
```

相关参数含义:

- **.type** 表示这个channel测量的数据类型, 此例中 (accelerometer), 我们将他设置为 IIO_ACCEL. type还可以是: IIO_LIGHT, IIO_VOLTAGE ..........

- **.modifier** 表示这个channel是否使用modifier, 如果用的话将会设置到**.channel2**中 (IIO_MOD_X, IIO_MOD_Y, IIO_MOD_Z 对应 xyz 轴)

- **.scan_index** 和 **.scan_type** 用于标明buffer中的elements, 这个和buffer trigger有关, 我们将在后面讨论

- **.info_mask_separate** 和 **.info_mask_shared_by_type** 标明这个channel将会暴露出那些信息. 这将会被所有相同type的channel所共享(indicate what information is to be exported that is specific to this channel, respectively that is shared by all channels of the same type) 本例中, 我们用了 IIO_CHAN_INFO_RAW, IIO_CHAN_INFO_CALIBBIAS, IIO_CHAN_INFO_SCALE, IIO_CHAN_INFO_SAMP_FREQ. 除此之外, iio还定义了很多其他的mask

但用户读 in_accel_scale 这个文件是, 系统会调用该驱动的read_raw 回调函数, 并传入值为IIO_CHAN_INFO_SCALE的参数mask. 当读取文件 in_accel_x_raw 时, 会调用read_raw回调函数, 此时mask的值为IIO_CHAN_INFO_RAW, 更多细节可以参考[这篇文档](https://git.kernel.org/pub/scm/linux/kernel/git/gregkh/staging.git/tree/Documentation/ABI/testing/sysfs-bus-iio)

有一篇关于IIO介绍的非常好的文章, [PPT可以在这里看到](https://archive.fosdem.org/2012/schedule/event/693/127_iio-a-new-subsystem.pdf)

其他有用的信息:

* [IIO mailing list](http://vger.kernel.org/vger-lists.html#linux-iio)

- [#linux-iio IRC channel of irc.oftc.net](http://webchat.oftc.net/?nick=&channels=%23linux-iio&uio=d4)



---------

# IIO triggered buffers

原文: https://iiobits.wordpress.com/

我们先看下trigger是如何在IIO子系统中使用的, 一个tirgger可以通过注册并将自己设置到 iio_device->trig 中来和一个IIO设备产生关联. 

我们看下Kernel暴露给IIO trigger的API. 为了分配一个trigger, 我们可以使用类似如下的代码:

```c
struct iio_trigger *tirg = iio_allocate_trigger("foo");
```

这里面比较重要的一个字段是 `.ops`, 他是 **struct iio_trigger_ops** 代表了一个iio_trigger的operations. 这个里面最重要的是 `.owner`和`.set_triggered_state`, 负责**开/关**这个trigger. 当这些都准备好后, 我们就可以调用**iio_trigger_register**来将该trigger注册上去了.

当前trigger值用在IIO中来填充software buffer. 任何支持**INDIO_BUFFER_TRIGGERED**的设备, 系统都会自动为他们生成consumer interface.

**iio_dev** 有一个字段叫 `.poolfunc`, 对应的函数会在每次数据转换时被trigger, 他的作用是从设备中检索数据,并填入buffer中, 因此 buffer 和 trigger 在IIO子系统中是紧密相连的


IIO中有两种buffer:

- [based on kfifo](http://lxr.free-electrons.com/source/drivers/iio/kfifo_buf.c#L12)
- [ring buffers](http://lxr.free-electrons.com/source/drivers/staging/iio/ring_generic.h?v=2.6.34#L113)

设置triggered buffer的helper func可以在这里找到: **drivers/iio/industrialio-triggered-buffer.c**. 

这里有一个重要的函数**iio_triggered_buffer_setup**, 他负责alloc buffer, 设置pollfunc, 以及将buf注册到IIO



举个[kxcj-1013](http://lxr.free-electrons.com/source/drivers/iio/accel/kxcjk-1013.c)的栗子:

```c
ret = iio_triggered_buffer_setup(indio_dev,
                                 iio_pollfunc_store_time,
                                 kxcjk1013_trigger_handler,
                                 NULL);
```

想知道[kxcjk1013_trigger_handler](http://lxr.free-electrons.com/source/drivers/iio/accel/kxcjk-1013.c#L943) 是如何实现的, 可以看[这里](http://lxr.free-electrons.com/source/drivers/iio/accel/kxcjk-1013.c#L943)



