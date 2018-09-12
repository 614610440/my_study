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
