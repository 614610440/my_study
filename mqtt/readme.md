# Linux mqtt

## 安装 Mosquitto
```shell
# 引入mosquitto仓库并更新
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update

# 执行以下命令安装mosquitto包(服务端)
sudo apt-get install mosquitto

#  安装mosquitto开发包
sudo apt-get install libmosquitto-dev

# 安装mosquitto客户端
sudo apt-get install mosquitto-clients

# 查询mosquitto是否正确运行
sudo service mosquitto status 
```