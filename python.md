#### python 学习记录


#### ubantu装多版本python
> 安装pyenv  
> + **git clone git://github.com/yyuu/pyenv.git ~/.pyenv** 
> + **echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc**  
> + **echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc**  
> + **echo 'eval "$(pyenv init -)"' >> ~/.bashrc**  
> + **exec $SHELL -l**  
>
> 查看可以安装的版本 **pyenv install --list**  
> 安装依赖项  
> + **sudo apt-get install libc6-dev gcc**
> + **sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm**
>  
> 安装 **pyenv install 3.4.3 -v**  
> 对数据库进行更新 **pyenv rehash**  
> 查看当前已安装版本 **pyenv versions**  其中 * 是系统自带版本  
> 设置全局的python版本 **pyenv global 3.4.3**  
> [参考](http://www.cnblogs.com/ningvsban/p/4384995.html)

#### pip加速
> [参考: https://www.cnblogs.com/microman/p/6107879.html](https://www.cnblogs.com/microman/p/6107879.html)
> + 新版ubuntu要求使用https源，要注意。  
>> 清华：https://pypi.tuna.tsinghua.edu.cn/simple  
>> 阿里云：http://mirrors.aliyun.com/pypi/simple/  
>> 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/  
>> 华中理工大学：http://pypi.hustunique.com/  
>> 山东理工大学：http://pypi.sdutlinux.org/   
>> 豆瓣：http://pypi.douban.com/simple/   
>  
> + 临时使用可以在使用pip的时候加参数-i https://pypi.tuna.tsinghua.edu.cn/simple  
  例如：**pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider** ，这样就会从清华这边的镜像去安装pyspider库。  
> + Linux下，修改 ~/.pip/pip.conf
>>  [global]
>> index-url = https://pypi.tuna.tsinghua.edu.cn/simple
>> [install]
>> trusted-host=mirrors.aliyun.com
>  
> + windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini。内容同上。
