## 配置zbar

#### 安装依赖 
````
sudo apt-get install python-gtk2-dev
sudo apt-get install libzbar-dev

# 安装libjpeg9来支持扫描jpg
sudp apt-get install libjpeg9

# 安装imagemagick
sudp apt-get install imagemagick

#python zbar
pip install zbar
````

#### 测试
> 1. 引用zbar, **python**, **import zbar**

#### 命令行解析图片
> 1. 安装zbar-tools, **sudo apt install zbar-tools**
> 2. **zbarimg *.jpg**

#### 测试代码
> [zbar_test.cpp](cpp/zbar_test.cpp)  
