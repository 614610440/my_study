# 学校VPN配置

## 方法一：  
```shell
sudo add-apt-repository ppa:nm-l2tp/network-manager-l2tp  
sudo apt-get update    
sudo apt-get install network-manager-l2tp  
sudo apt-get install network-manager-l2tp-gnome   
```

## 方法二：  
```shell
cd ~/  
mkdir tools  
cd tools  
https://github.com/nm-l2tp/network-manager-l2tp.git  

#### 添加编译依赖

sudo apt install git intltool libtool network-manager-dev libnm-util-dev libnm-glib-dev libnm-glib-vpn-dev libnm-gtk-dev libnm-dev libnma-dev ppp-dev libdbus-glib-1-dev libsecret-1-dev libgtk-3-dev libglib2.0-dev xl2tpd strongswan
 
#### 编译安装

cd network-manager-l2tp  
./autogen.sh  
./configure --disable-static --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib/x86_64-linux-gnu --libexecdir=/usr/lib/NetworkManager --localstatedir=/var --with-pppd-plugin-dir=/usr/lib/pppd/2.4.7  
make  
sudo make install  
```
 
## 设置vpn
> 菜单-设置-网络连接-增加-第二层隧道协议L2TP-新建-VPN选项卡  
> 连接名称填写WIT VPN  
> 网关填写59.172.155.68  
> 用户名填写你在学校网络中心开通的上网，一般为学号  
> 保存后关闭 
 
在上网方式选择中点击VPN连接-WIT VPN
输入上网帐号密码