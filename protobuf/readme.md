# prototest
protobuf嵌入测试, 在网络通讯系统中，protobuf能够提升通讯效率。消息嵌套可以实现传输较为复杂的消息。

## 安装
```
# 依赖
sudo apt-get install g++ git automake libtool libgc-dev bison flex libfl-dev libgmp-dev libboost-dev libboost-iostreams-dev pkg-config python python-scapy python-ipaddr tcpdump cmake autoconf

# 安装
./autogen.sh
./configure --prefix=/usr/local/
```

## 使用
```shell
 #生成python文件
protoc --python_out=./ test.proto
```