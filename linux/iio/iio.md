# iio

原文地址： https://www.kernel.org/doc/html/v4.17/driver-api/iio/index.html

## Core elements

### Industrial I/O Devices

* struct iio_dev - industrial I/O device

* iio_device_alloc() - alocate an iio_dev from a driver

* iio_device_free() - free an iio_dev from a driver

* iio_device_register() - register a device with the IIO subsystem

* iio_device_unregister() - unregister a device from the IIO subsystem



一个iio设备通常对应一个单独的硬件传感器， 并提供所有足以让驱动控制该设备的信息， 首先让我们看看iio device中的功能， 然后再看设备驱动如何利用iio



有两种方式和iio驱动交互

1. /sys/bus/iio/iio:deviceX/ 代表一个硬件传感器，该芯片的所有data channels都将存放与此
2. /dev/iio:deviceX， 这是一个字符设备的节点， 用于buffer数据的交互以及实现信息的检索

一个典型的iio驱动会将自己注册为i2c或者spi驱动，并实现probe和remove函数

在`probe`函数中

1. 调用`iio_device_alloc()`， 在内存中创建一个iio设备
2. 初始化iio device的内部数据（例如 设备名， 设备channel）
3. 调用`iio_device_register()` 讲该设备注册到iio core中， 之后就可以接受用户层发来的请求了

在`remove`中

1. `iio_device_unregister()`, 从 iio core 中注销掉
2. `iio_device_free()` 释放该设备结构本身所占用内存

### IIO device sysfs interface

可以通过sysfs来访问和设置相关参数， 假设某个device 的idx为X， 那么他的参数可以在 `/sys/bus/iio/iio:deviceX/`中找到， 常用的参数如下

* name， 描述该物理芯片
* dev， 展示该X设备的 major:minor 
* sampling_frequency_avaiable, 
* 标准的可以使用的参数可以在内核代码的` Documentation/ABI/testing/sysfs-bus-iio`中找到

### IIO device channels

`struct iio_chan_spec` 描述一个single channel

一个iio device channel表示一个数据channel， 一个IIO 设备可以有一个或者多个channel， 比方说

* 一个温度传感器可能只有一个channel用于温度的测量
* 一个光纤传感器有两个channels， 分别表示可见和红外的光谱
* 一个加速度传感器可能可以有3个channels分别表示在X，Y，Z轴上的加速度

一个iio channel用`struct iio_chan_spec`来表示， 例如一个温度传感器驱动可以用下面的方式来设置他的channel

```c
static const struct iio_chan_spec temp_channel[] = {
     {
         .type = IIO_TEMP,
         .info_mask_separate = BIT(IIO_CHAN_INFO_PROCESSED),
     },
};
```

Channel的sysfs参数通常用bitmask的方式来表达， 按照他们share的信息的不同， 可以用下面的mask

* info_mask_separate, 该参数只用于这个channel
* info_mask_shared_by_type, 该参数将被所有同类型的channel所共享

* info_mask_shared_by_dir, 该参数将被所有同方向的channel所共享
* info_mask_shared_by_all, 该参数将用于所有的channel

当有多个channel是同一个类型时， 我们有两种方法来区分他们

* 将`.modifier`设置为1， 通过`.channel2`来区分，例如光纤传感器有两个channels， 一个用于红外光，一个用于可见光和红外光
* 将`.indexed`设置为1， 此时将通过`.channel`来区分， 该字段将用index来表示

下面是两个例子

```c
·	
static const struct iio_chan_spec light_channels[] = {
        {
                .type = IIO_INTENSITY,
                .modified = 1,
                .channel2 = IIO_MOD_LIGHT_IR,
                .info_mask_separate = BIT(IIO_CHAN_INFO_RAW),
                .info_mask_shared = BIT(IIO_CHAN_INFO_SAMP_FREQ),
        },
        {
                .type = IIO_INTENSITY,
                .modified = 1,
                .channel2 = IIO_MOD_LIGHT_BOTH,
                .info_mask_separate = BIT(IIO_CHAN_INFO_RAW),
                .info_mask_shared = BIT(IIO_CHAN_INFO_SAMP_FREQ),
        },
        {
                .type = IIO_LIGHT,
                .info_mask_separate = BIT(IIO_CHAN_INFO_PROCESSED),
                .info_mask_shared = BIT(IIO_CHAN_INFO_SAMP_FREQ),
        },
   }
```

此配置将产生两个文件

* /sys/bus/iio/iio:deviceX/in_intensity_ir_raw
* /sys/bus/iio/iio:deviceX/in_intensity_both_raw

此外还会生成

* /sys/bus/iio/iio:deviceX/in_illuminance_input

以及

* /sys/bus/iio/iio:deviceX/sampling_frequency

```c
static const struct iio_chan_spec light_channels[] = {
        {
                .type = IIO_VOLTAGE,
                .indexed = 1,
                .channel = 0,
                .info_mask_separate = BIT(IIO_CHAN_INFO_RAW),
        },
        {
                .type = IIO_VOLTAGE,
                .indexed = 1,
                .channel = 1,
                .info_mask_separate = BIT(IIO_CHAN_INFO_RAW),
        },
}
```

该配置将产生两个文件

* /sys/bus/iio/devices/iio:deviceX/in_voltage0_raw, representing voltage measurement for channel 0.

* /sys/bus/iio/devices/iio:deviceX/in_voltage1_raw, representing voltage measurement for channel 1.





-------------------------------------------------------------------------

## Buffers

* struct iio_buffer — general buffer structure
* iio_validate_scan_mask_onehot() — Validates that exactly one channel is selected
* iio_buffer_get() — Grab a reference to the buffer
* iio_buffer_put() — Release the reference to the buffer

### IIO buffer sysfs interface

一个iio buffer的attributes目录在`/sys/bus/iio/iio:deviceX/buffer/*` 一般包含如下参数

* length 可以存放的数据大小
* enable 是否在捕获数据

### IIO buffer setup

在buffer中用于读取channel的元信息我们称为`scan element`, 通过` /sys/bus/iio/iio:deviceX/scan_elements/*`来进行scan element的配置， 通常包含如下参数

* enable, 使能一个channel， 只有当其为非零的时候， 被触发的捕获才会包含该channel的数据
* type， 描述buffer中scan element(description of the scan element data storage within the buffer and hence the form in which it is read from user space)， 格式为`[be|le]:[s|u]bits/storagebitsXrepeat[>>shift]`
  * be/le: big/little endian
  * s/u: signed/unsigned (用2的补码)
  * bits： 有效的data bits个数
  * storagebits： padding之后在buffer中占用的bit 个数
  * shift： 如果设置了， 表示要先mask out掉无效的bits
  * repeat： 表示bits/storagebits的重复次数， 如果为0， 或者1， repeat的值将会被忽略（不起作用？）

例如， 一个3轴加速度传感器驱动，12bit的数据精度， 他们的数据将会存放在两个8bit的寄存器中

```
  7   6   5   4   3   2   1   0
+---+---+---+---+---+---+---+---+
|D3 |D2 |D1 |D0 | X | X | X | X | (LOW byte, address 0x06)
+---+---+---+---+---+---+---+---+

  7   6   5   4   3   2   1   0
+---+---+---+---+---+---+---+---+
|D11|D10|D9 |D8 |D7 |D6 |D5 |D4 | (HIGH byte, address 0x07)
+---+---+---+---+---+---+---+---+
```

他的每一个轴的 scan element type 如下

```
$ cat /sys/bus/iio/devices/iio:device0/scan_elements/in_accel_y_type
le:s12/16>>4
```

其表示，buffer中的数据格式为： little endian， 有符号数， 占用16bit， 高12bit有效，需要右移4个bit

驱动应该负责初始化 iio_chan_spec 中的如下部分

```c
struct iio_chan_spec {
/* other members */
        int scan_index
        struct {
                char sign;
                u8 realbits;
                u8 storagebits;
                u8 shift;
                u8 repeat;
                enum iio_endian endianness;
       } scan_type;
};
```

我们上面举例的那个3轴传感器的初始化代码如下

```c
struct struct iio_chan_spec accel_channels[] = {
        {
                .type = IIO_ACCEL,
                .modified = 1,
                .channel2 = IIO_MOD_X,
                /* other stuff here */
                .scan_index = 0,
                .scan_type = {
                        .sign = 's',
                        .realbits = 12,
                        .storagebits = 16,
                        .shift = 4,
                        .endianness = IIO_LE,
                },
        }
        /* similar for Y (with channel2 = IIO_MOD_Y, scan_index = 1)
         * and Z (with channel2 = IIO_MOD_Z, scan_index = 2) axis
         */
 }
```

上面代码中的 **scan_index** 在内存中enable的channel的存放顺序， 低 **scan_index**的channel将会被放在高 **scan_index** channel的后面， 每一个 **scan_index**必须是唯一的

如果我们将 **scan_index**设置为**-1**， 表示这个channel不支持数据捕获， 此时该channel的scan_elements目录将为空



-------------------

## Triggers

* struct iio_trigger — industrial I/O trigger device
* devm_iio_trigger_alloc() — Resource-managed iio_trigger_alloc
* devm_iio_trigger_free() — Resource-managed iio_trigger_free
* devm_iio_trigger_register() — Resource-managed iio_trigger_register
* devm_iio_trigger_unregister() — Resource-managed iio_trigger_unregister
* iio_trigger_validate_own_device() — Check if a trigger and IIO device belong to the same device

在很多场景下，如果驱动可以通过一些外部事件(trigger)触发来捕获数据，而不是周期性的轮询的话，那是极好的。

如果一个IIO的硬件设备可以产生event (e.g. data ready或者threshold exceeded )，那么该iio device所对应的driver就可以提供 IIO trigger， 或者也可以由一个单独的驱动用一个独立的中断源来提供trigger(e.g. GPIO连到外部系统， 时钟中断， 甚至用户往sysfs的某个特定文件写数据)。 一个trigger可以让多个传感器发起数据捕获， 他可以和传感器本身毫无关联

### IIO trigger sysfs interface

有两个地方可以触发triggers

* /sys/bus/iio/devices/triggerY/*, 当我们将一个IIO trigger 注册到 IIO core的时候， 这个文件就会创建出来，并对应到Idx为Y的trigger， 因为type不同的trigger，区别会非常大， 所有我们只看下少量的标准参数：
  * name, trigger name that can be later used for association with a device.
  * sampling_frequency, some timer based triggers use this attribute to specify the frequency for trigger calls.
* */sys/bus/iio/devices/iio:deviceX/trigger/*, 当一个设备支持triggered buffer时， 该目录就会被创建。 我们可以通过将trigger‘s的name写入`current_trigger`来将一个trigger与我们的device联系起来

### IIO trigger setup

举个栗子：

```c
struct iio_trigger_ops trigger_ops = {
    .set_trigger_state = sample_trigger_state,
    .validate_device = sample_validate_device,
}

struct iio_trigger *trig;

/* first, allocate memory for our trigger */
trig = iio_trigger_alloc(dev, "trig-%s-%d", name, idx);

/* setup trigger operations field */
trig->ops = &trigger_ops;

/* now register the trigger with the IIO core */
iio_trigger_register(trig);
```

### IIO trigger ops

* struct iio_trigger_ops — operations structure for an iio_trigger.

  我们需要给她设置一组操作

  * set_trigger_state, switch the trigger on/off on demand.

  * validate_device, function to validate the device when the current trigger gets changed.

### Triggered Buffers

前面介绍了buffer 和 trigger，现在看看怎么将他们联系起来

### IIO triggered buffer setup
* iio_triggered_buffer_setup() — Setup triggered buffer and pollfunc
* iio_triggered_buffer_cleanup() — Free resources allocated by iio_triggered_buffer_setup()
* struct iio_buffer_setup_ops — buffer setup related callbacks

举个栗子：

```c
const struct iio_buffer_setup_ops sensor_buffer_setup_ops = {
  .preenable    = sensor_buffer_preenable,
  .postenable   = sensor_buffer_postenable,
  .postdisable  = sensor_buffer_postdisable,
  .predisable   = sensor_buffer_predisable,
};

irqreturn_t sensor_iio_pollfunc(int irq, void *p)
{
    pf->timestamp = iio_get_time_ns((struct indio_dev *)p);
    return IRQ_WAKE_THREAD;
}

irqreturn_t sensor_trigger_handler(int irq, void *p)
{
    u16 buf[8];
    int i = 0;

    /* read data for each active channel */
    for_each_set_bit(bit, active_scan_mask, masklength)
        buf[i++] = sensor_get_data(bit)

    iio_push_to_buffers_with_timestamp(indio_dev, buf, timestamp);

    iio_trigger_notify_done(trigger);
    return IRQ_HANDLED;
}

/* setup triggered buffer, usually in probe function */
iio_triggered_buffer_setup(indio_dev, sensor_iio_polfunc,
                           sensor_trigger_handler,
                           sensor_buffer_setup_ops);
```

需要注意的是

* **iio_buffer_setup_ops**, the buffer setup functions to be called at predefined points in the buffer configuration sequence (e.g. before enable, after disable). If not specified, the IIO core uses the default iio_triggered_buffer_setup_ops.
* **sensor_iio_pollfunc**, 该函数将会在poll 函数的上半部被调用. 他工作在中断上下文，请尽可能在里面做最少的事情。因为通常情况下，只需要获取时间戳， 所以我们可以直接使用IIO core中预先帮我们定义的iio_pollfunc_store_time()函数 
* **sensor_trigger_handler**, 在下半部被调用，工作在kernel线程中，通常是从设备中读取数据，并将之前获得的时间戳一起存入buffer中



-------

## HW consumer

IIO设备可以直接和其他的硬件设备相连，此时IIO provider和consumer之间的buffer将由硬件来处理。IIO HW consumer提供一些方法来链接IIO devices，不需要软件buffer， 可以从`drivers/iio/buffer/hw-consumer.c`中找到具体实现

* struct iio_hw_consumer — Hardware consumer structure
* iio_hw_consumer_alloc() — Allocate IIO hardware consumer
* iio_hw_consumer_free() — Free IIO hardware consumer
* iio_hw_consumer_enable() — Enable IIO hardware consumer
* iio_hw_consumer_disable() — Disable IIO hardware consumer

### HW consumer setup

举个栗子：

```c
static struct iio_hw_consumer *hwc;

static const struct iio_info adc_info = {
        .read_raw = adc_read_raw,
};

static int adc_read_raw(struct iio_dev *indio_dev,
                        struct iio_chan_spec const *chan, int *val,
                        int *val2, long mask)
{
        ret = iio_hw_consumer_enable(hwc);

        /* Acquire data */

        ret = iio_hw_consumer_disable(hwc);
}

static int adc_probe(struct platform_device *pdev)
{
        hwc = devm_iio_hw_consumer_alloc(&iio->dev);
}
```














