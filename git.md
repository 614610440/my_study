# git教程
> [配置Git](#配置Git)  
> [使用](#使用)  
> [查看修改历史](#查看修改历史)  
> [Tags](#Tags)   
> [删除文件](#删除文件)  
> [错误解决](#错误解决)  
> [目录忽略](#目录忽略)  

## 配置Git
```shell
ssh-keygen -t rsa -C "614610440@qq.com" # 一路默认回车。  

# 进入~/.ssh文件夹， 
# 打开id_rsa.pub,复制里面的key, 
# 回到github, 进入Account Settings, 填写SSH keys  

ssh -T git@github.com # 验证是否连接成功  

# 设置用户名和邮箱  
git config --global user.name "wxx"
git config --global user.email "614610440@qq.com"  

# 进入本地库(my_study), 
git init # 初始化库
git remote add origin
git@github.com:614610440/my_study.git  #用户名和库名。  
```

## 使用
```shell
git add filename        # 添加要上传的文件
git commit -m "commit"  # 编辑更改信息
git pull origin master  # 将库同步到本地库
git push origin master  # 上传库
```

## 查看修改历史
> 将github.com改为github.githistory.xyz  

## Tags
```shell
git tag -a version_1.0 -m 'first version' # 创建tag
git push origin version_1.0
git push origin --delete tag <tagname>   # 删除远程tag
git tag -d <tagname>                     #删除本地tag
```

## Branch
```shell
# 创建branch
git branch your_branch

# 将分支切换到your_branch
git checkout your_branch 

# 查看所有分支列表，包括本地和远程
git branch -a

#　删除your_branch分支，如果在分支中有一些未merge的提交，那么会删除分支失败，此时可以使用 git branch -D your_branch：强制删除your_branch分支，
git branch -d your_branch

#　给分支重命名
git branch -m oldName newName
```

## checkout
```shell
# 放弃单个文件的修改
git checkout filename 

# 放弃当前目录下的修改
git checkout

# 将分支切换到your_branch
git checkout your_branch 
```

## 删除文件
```shell
git rm --cached -r useless_file  
git commit -m "remove directory from remote repository"  
git push  
```

## 错误解决:

#### fatal: 远程 origin 已经存在。
```shell
git remote rm origin  
```

#### error: commit is not possible because you have unmerged files. local文件冲突，
```shell
git add -u
git commit #解决冲突文件  
git reset --hard FETCH_HEAD #（可能会删掉一些新建文件，先备份再复原）。  
```

#### You are not currently on a branch.  
> + [解决方案](https://blog.csdn.net/xinguan1267/article/details/39028789)  

## 目录忽略( .gitignore)
```txt
#               表示此为注释,将被Git忽略  
*.a             表示忽略所有 .a 结尾的文件  
!lib.a          表示但lib.a除外  
/TODO           表示仅仅忽略项目根目录下的 TODO 文件，不包括 subdir/TODO  
build/          表示忽略 build/目录下的所有文件，过滤整个build文件夹；  
doc/*.txt       表示会忽略doc/notes.txt但不包括 doc/server/arch.txt  
   
bin/:           表示忽略当前路径下的bin文件夹，该文件夹下的所有内容都会被忽略，不忽略 bin 文件  
/bin:           表示忽略根目录下的bin文件  
/*.c:           表示忽略cat.c，不忽略 build/cat.c  
debug/*.obj:    表示忽略debug/io.obj，不忽略 debug/common/io.obj和tools/debug/io.obj  
**/foo:         表示忽略/foo,a/foo,a/b/foo等  
a/**/b:         表示忽略a/b, a/x/b,a/x/y/b等  
!/bin/run.sh    表示不忽略bin目录下的run.sh文件  
*.log:          表示忽略所有 .log 文件  
config.php:     表示忽略当前路径的 config.php 文件  
   
/mtk/           表示过滤整个文件夹  
*.zip           表示过滤所有.zip文件  
/mtk/do.c       表示过滤某个具体文件  
   
被过滤掉的文件就不会出现在git仓库中（gitlab或github）了，当然本地库中还有，只是push的时候不会上传。  
   
需要注意的是，gitignore还可以指定要将哪些文件添加到版本管理中，如下：  
!*.zip  
!/mtk/one.txt  
   
唯一的区别就是规则开头多了一个感叹号，Git会将满足这类规则的文件添加到版本管理中。为什么要有两种规则呢？  
想象一个场景：假如我们只需要管理/mtk/目录中的one.txt文件，这个目录中的其他文件都不需要管理，那么.gitignore规则应写为：：  
/mtk/*  
!/mtk/one.txt  
   
假设我们只有过滤规则，而没有添加规则，那么我们就需要把/mtk/目录下除了one.txt以外的所有文件都写出来！  
注意上面的/mtk/*不能写为/mtk/，否则父目录被前面的规则排除掉了，one.txt文件虽然加了!过滤规则，也不会生效！  
   
----------------------------------------------------------------------------------  
还有一些规则如下：  
fd1/*  
说明：忽略目录 fd1 下的全部内容；注意，不管是根目录下的 /fd1/ 目录，还是某个子目录 /child/fd1/ 目录，都会被忽略；  
   
/fd1/*  
说明：忽略根目录下的 /fd1/ 目录的全部内容；  
   
/*  
!.gitignore  
!/fw/   
/fw/*  
!/fw/bin/  
!/fw/sf/  
说明：忽略全部内容，但是不忽略 .gitignore 文件、根目录下的 /fw/bin/ 和 /fw/sf/ 目录；注意要先对bin/的父目录使用!规则，使其不被排除。  
```

##  参考：
> + [Github 简明教程](http://www.runoob.com/w3cnote/git-guide.html)  
> + [Git忽略提交规则](https://www.cnblogs.com/kevingrace/p/5690241.html)  

