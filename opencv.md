#### ubantu下OpenCV配置

> 1. 下载包，解压，在包中创建build  
> 2. 进入build,自定义路径，**cmake -D WITH_CUDA=OFF -D WITH_OPENGL=OFF  -D CMAKE_INSTALL_PREFIX=/home/xxx/lib ..** ，此阶段会自动检测缺失依赖并自动下载。
> 3. **make**  
> 4. **sudo make install**  
