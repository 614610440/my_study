# Linux常用命令

#### 目录
> [wathc](#watch)
> [lightdm](#lightdm)


#### watch
> watch -n 5 nvidia-smi （其中，5表示每隔5秒刷新一次终端的显示结果）
>  -d或--differences  用-d或--differences 选项watch 会高亮显示变化的区域。 而-d=cumulative选项会把变动过的地方(不管最近的那次有没有变动)都高亮显示出来。
>  -t 或-no-title  会关闭watch命令在顶部的时间间隔,命令，当前时间的输出。

#### lightdm
> sudo service lightdm stop
> 禁用X-Window
