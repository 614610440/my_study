# git教程

## 配置Git
> + **ssh-keygen -t rsa -C "614610440@qq.com"**， 一路默认回车。
> + 进入~/.ssh文件夹， 打开id_rsa.pub,复制里面的key, 回到github, 进入Account Settings, 填写SSH keys
> + **ssh -T git@github.com** 验证是否连接成功
> + **git config --global user.name "wxx"**,  **git config --global user.email "614610440@qq.com"**,  设置用户名和邮箱  s
> + 进入本地库(my_study), **git init**初始化库, **git remote add origin git@github.com:614610440/my_study.git**, 用户名和库名。

## 使用
> + 添加要上传的文件， **git add filename**
> + 编辑更改信息， **git commit -m "commit"**
> + 将库同步到本地库， **git pull origin master**
> + 上传库, **git push origin master**

## 删除文件
> + git rm --cached -r useless_file
> + git commit -m "remove directory from remote repository"
> + git push

## 错误解决:

#### fatal: 远程 origin 已经存在。
> **git remote rm origin**

##  参考：
> + [Github 简明教程](http://www.runoob.com/w3cnote/git-guide.html)
