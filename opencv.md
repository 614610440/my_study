#### ubantu下OpenCV配置

1.安装官方给的opencv依赖包

````
sudo apt-get install build-essential  
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
# 处理图像所需的包 
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev  
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev  
 # 处理视频所需的包 
sudo apt-get install libxvidcore-dev libx264-dev 
 # 优化opencv功能 
sudo apt-get install libatlas-base-dev gfortran 
sudo apt-get install ffmpeg  
````

```shell
#  下载包，解压，在包中创建build  
# 进入build
# cmake, 进行配置此阶段会自动检测缺失依赖并自动下载。

# 直接cmake
cmake ..

# 相关参数
# -D WITH_CUDA=OFF   //不需要CUDA
# -D WITH_OPENGL=OFF  //不需要OPENGL
# -D CMAKE_INSTALL_PREFIX=/home/xxx/lib 
# 不需要CUDA及OpenGL, 设置安装目录
cmake -D WITH_CUDA=OFF -D WITH_OPENGL=OFF -D CMAKE_INSTALL_PREFIX=/home/xxx/lib ..

# 自定义安装目录方便不同版本切换

# 编译 
make

# 安装
sudo make install


# sudo gedit .bashrc添加目录
export PKG_CONFIG_PATH=/home/wxx/lib/opencv-3.4.1/lib/pkgconfig  
export LD_LIBRARY_PATH=/home/wxx/lib/opencv-3.4.1/lib   
sudo sh -c 'echo "/home/wxx/lib/opencv-3.4.1/lib" > /etc/ld.so.conf.d/opencv.conf'

# 安装完成后通过查看 opencv 版本验证是否安装成功：
pkg-config --modversion opencv 

## 安装cuda版本(需要先装cuda)
cmake -D CMAKE_BUILD_TYPE=RELEASE -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_CUDA=ON -D ENABLE_FAST_MATH=1 -D CUDA_FAST_MATH=1 -D CUDA_NVCC_FLAGS="-D_FORCE_INLINES" -D WITH_CUBLAS=1 -D WITH_NVCUVID=OFF -D CMAKE_INSTALL_PREFIX=/home/wxx/lib/OpenCV3.1.1-gpu ..
```

## 安装Contrib
```
## 下载对应版本Contrib添加参数
 -D OPENCV_EXTRA_MODULES_PATH=…/…/opencv_contrib/modules …
```

## 错误及解决方案

#### fatal error: dynlink_nvcuvid.h: 没有那个文件或目录 #include <dynlink_nvcuvid.h> 
```shell
# cuda版本不同， 头文件不同，cmake时添加下面参数
-D WITH_NVCUVID=OFF
```

## QT 配置Opencv
```
INCLUDEPATH += /home/wxx/lib/Opencv3.4.0/include \
               /home/wxx/lib/Opencv3.4.0/include/opencv \
               /home/wxx/lib/Opencv3.4.0/include/opencv2 \

LIBS += /home/wxx/lib/Opencv3.4.0/lib/libopencv_highgui.so \
        /home/wxx/lib/Opencv3.4.0/lib/libopencv_core.so \
        /home/wxx/lib/Opencv3.4.0/lib/libopencv_imgcodecs.so \
        /home/wxx/lib/Opencv3.4.0/lib/libopencv_objdetect.so \
        /home/wxx/lib/Opencv3.4.0/lib/libopencv_imgproc.so \
        /home/wxx/lib/Opencv3.4.0/lib/libopencv_video.so \
        /home/wxx/lib/Opencv3.4.0/lib/libopencv_videoio.so \
```

#### 提示
1. OpenCV4.2 dnn支持cuda