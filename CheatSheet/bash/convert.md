### 使用convert将rawbuffer转换为png图片

1. 对于YUV420的转换  
```convert -size 640x480 -sampling-factor 4:2:0 -depth 8 yuv.yuv yuv.png```

1. 对于YUV422  
```ffmpeg -s 640x480 -pix_fmt yvyu422 -i yuv.yuv -f image2 -pix_fmt rgb24 yuv.png```


1. 对于RGB  
```convert -depth 8 -size 640x480 rgb:/tmp/pic.raw /tmp/pic2.png```


###### ffmpeg支持的 fmt
```
Pixel formats:
I.... = Supported Input  format for conversion
.O... = Supported Output format for conversion
..H.. = Hardware accelerated format
...P. = Paletted format
....B = Bitstream format
FLAGS NAME            NB_COMPONENTS BITS_PER_PIXEL
-----
IO... yuv420p                3            12
IO... yuyv422                3            16
IO... rgb24                  3            24
IO... bgr24                  3            24
IO... yuv422p                3            16
IO... yuv444p                3            24
IO... yuv410p                3             9
IO... yuv411p                3            12
IO... gray                   1             8
IO..B monow                  1             1
IO..B monob                  1             1
I..P. pal8                   1             8
IO... yuvj420p               3            12
IO... yuvj422p               3            16
IO... yuvj444p               3            24
..H.. xvmcmc                 0             0
..H.. xvmcidct               0             0
IO... uyvy422                3            16
..... uyyvyy411              3            12
IO... bgr8                   3             8
.O..B bgr4                   3             4
IO... bgr4_byte              3             4
IO... rgb8                   3             8
.O..B rgb4                   3             4
IO... rgb4_byte              3             4
IO... nv12                   3            12
IO... nv21                   3            12
IO... argb                   4            32
IO... rgba                   4            32
IO... abgr                   4            32
IO... bgra                   4            32
IO... gray16be               1            16
IO... gray16le               1            16
IO... yuv440p                3            16
IO... yuvj440p               3            16
IO... yuva420p               4            20
..H.. vdpau_h264             0             0
..H.. vdpau_mpeg1            0             0
..H.. vdpau_mpeg2            0             0
..H.. vdpau_wmv3             0             0
..H.. vdpau_vc1              0             0
IO... rgb48be                3            48
IO... rgb48le                3            48
IO... rgb565be               3            16
IO... rgb565le               3            16
IO... rgb555be               3            15
IO... rgb555le               3            15
IO... bgr565be               3            16
IO... bgr565le               3            16
IO... bgr555be               3            15
IO... bgr555le               3            15
..H.. vaapi_moco             0             0
..H.. vaapi_idct             0             0
..H.. vaapi_vld              0             0
IO... yuv420p16le            3            24
IO... yuv420p16be            3            24
IO... yuv422p16le            3            32
IO... yuv422p16be            3            32
IO... yuv444p16le            3            48
IO... yuv444p16be            3            48
..H.. vdpau_mpeg4            0             0
..H.. dxva2_vld              0             0
IO... rgb444le               3            12
IO... rgb444be               3            12
IO... bgr444le               3            12
IO... bgr444be               3            12
IO... ya8                    2            16
IO... bgr48be                3            48
IO... bgr48le                3            48
IO... yuv420p9be             3            13
IO... yuv420p9le             3            13
IO... yuv420p10be            3            15
IO... yuv420p10le            3            15
IO... yuv422p10be            3            20
IO... yuv422p10le            3            20
IO... yuv444p9be             3            27
IO... yuv444p9le             3            27
IO... yuv444p10be            3            30
IO... yuv444p10le            3            30
IO... yuv422p9be             3            18
IO... yuv422p9le             3            18
..H.. vda_vld                0             0
IO... gbrp                   3            24
IO... gbrp9be                3            27
IO... gbrp9le                3            27
IO... gbrp10be               3            30
IO... gbrp10le               3            30
I.... gbrp16be               3            48
I.... gbrp16le               3            48
IO... yuva420p9be            4            22
IO... yuva420p9le            4            22
IO... yuva422p9be            4            27
IO... yuva422p9le            4            27
IO... yuva444p9be            4            36
IO... yuva444p9le            4            36
IO... yuva420p10be           4            25
IO... yuva420p10le           4            25
IO... yuva422p10be           4            30
IO... yuva422p10le           4            30
IO... yuva444p10be           4            40
IO... yuva444p10le           4            40
IO... yuva420p16be           4            40
IO... yuva420p16le           4            40
IO... yuva422p16be           4            48
IO... yuva422p16le           4            48
IO... yuva444p16be           4            64
IO... yuva444p16le           4            64
..H.. vdpau                  0             0
IO... xyz12le                3            36
IO... xyz12be                3            36
..... nv16                   3            16
..... nv20le                 3            20
..... nv20be                 3            20
IO... yvyu422                3            16
..H.. vda                    0             0
I.... ya16be                 2            32
I.... ya16le                 2            32
..H.. qsv                    0             0
..H.. mmal                   0             0
..H.. d3d11va_vld            0             0
IO... rgba64be               4            64
IO... rgba64le               4            64
IO... bgra64be               4            64
IO... bgra64le               4            64
IO... 0rgb                   3            24
IO... rgb0                   3            24
IO... 0bgr                   3            24
IO... bgr0                   3            24
IO... yuva444p               4            32
IO... yuva422p               4            24
IO... yuv420p12be            3            18
IO... yuv420p12le            3            18
IO... yuv420p14be            3            21
IO... yuv420p14le            3            21
IO... yuv422p12be            3            24
IO... yuv422p12le            3            24
IO... yuv422p14be            3            28
IO... yuv422p14le            3            28
IO... yuv444p12be            3            36
IO... yuv444p12le            3            36
IO... yuv444p14be            3            42
IO... yuv444p14le            3            42
IO... gbrp12be               3            36
IO... gbrp12le               3            36
IO... gbrp14be               3            42
IO... gbrp14le               3            42
IO... gbrap                  4            32
I.... gbrap16be              4            64
I.... gbrap16le              4            64
IO... yuvj411p               3            12
I.... bayer_bggr8            3             8
I.... bayer_rggb8            3             8
I.... bayer_gbrg8            3             8
I.... bayer_grbg8            3             8
I.... bayer_bggr16le         3            16
I.... bayer_bggr16be         3            16
I.... bayer_rggb16le         3            16
I.... bayer_rggb16be         3            16
I.... bayer_gbrg16le         3            16
I.... bayer_gbrg16be         3            16
I.... bayer_grbg16le         3            16
I.... bayer_grbg16be         3            16
IO... yuv440p10le            3            20
IO... yuv440p10be            3            20
IO... yuv440p12le            3            24
IO... yuv440p12be            3            24
IO... ayuv64le               4            64
..... ayuv64be               4            64
..H.. videotoolbox_vld       0             0

```