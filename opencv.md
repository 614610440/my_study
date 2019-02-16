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
> 1. 下载包，解压，在包中创建build  
> 2. 进入build,自定义路径，**cmake -D WITH_CUDA=OFF -D WITH_OPENGL=OFF  -D CMAKE_INSTALL_PREFIX=/home/xxx/lib ..** ，此阶段会自动检测缺失依赖并自动下载。
> 3. **make**  
> 4. **sudo make install**  
> 5. sudo gedit .bashrc二选一
> export PKG_CONFIG_PATH=/home/wxx/lib/opencv-3.4.1/lib/pkgconfig  
> export LD_LIBRARY_PATH=/home/wxx/lib/opencv-3.4.1/lib   
> #PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/home/wxx/lib/opencv-3.4.1/lib/pkgconfig  
> #export PKG_CONFIG_PATH  
> or
> export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH  
> export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

安装完成后通过查看 opencv 版本验证是否安装成功：

pkg-config --modversion opencv  

