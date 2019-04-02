# GO 学习

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