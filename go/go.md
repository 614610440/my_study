# GO 学习

## 目录
[string,int互相转](#string,int互相转)

#### Ubantu安装GO
```
sudo apt-get install golang-go
```

#### 使用
> **gedit helloWorld.go**  
```go
package main

import (
    "fmt"
    "runtime"
)

func main() {
    fmt.Println("Hellow World!", runtime.Version())
}
```
> **go run helloWorld.go**  
> [helloWorld.go](helloWorld.go)  

#### string,int互相转
```go
// string转成int：
int, err := strconv.Atoi(string)

// string转成int64：
int64, err := strconv.ParseInt(string, 10, 64) 

// int转成string：
string := strconv.Itoa(int)

// int64转成string：
string := strconv.FormatInt(int64,10) 

```
