#### ubantu下OpenCV配置

> 1. 下载包，解压，在包中创建build  
> 2. 进入build,自定义路径，**cmake -D WITH_CUDA=OFF -D WITH_OPENGL=OFF  -D CMAKE_INSTALL_PREFIX=/home/xxx/lib ..** ，此阶段会自动检测缺失依赖并自动下载。
> 3. **make**  
> 4. **sudo make install**  
> 5. sudo gedit .bashrc二选一
> export PKG_CONFIG_PATH=/home/wxx/lib/opencv-3.4.1/lib/pkgconfig
> export LD_LIBRARY_PATH=/home/wxx/lib/opencv-3.4.1/lib
> #PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/home/wxx/lib/opencv-3.4.1/lib/pkgconfig
> #export PKG_CONFIG_PATH
