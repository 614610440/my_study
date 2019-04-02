package main

import (
    "fmt"
    "runtime"
)

type Books struct{
    titile string
    author string
    subject string
    book_id string
}

func functionTest()(string, string, string, string, string, string){
    var a = "I'm A"
    b := "I'm B"
    var c,d = "I'm C", "I'm D"
    e,f := "I'm E", "I'm F"
    
    return a, b, c, d, e, f
}

func main() {
    var h = "Hellow World!"
    a := "No var"
    fmt.Println(h, runtime.Version())
    fmt.Println(a)

    result0, result1, result2, result3, result4, result5 := functionTest()

    fmt.Println(result0)
    fmt.Println(result1)
    fmt.Println(result2)
    fmt.Println(result3)
    fmt.Println(result4)
    fmt.Println(result5)

    _,_,result2_1,_,_,result5_1 := functionTest()
    fmt.Println(result2_1)
    fmt.Println(result5_1)


    // 结构体
    book := Books{"Go 语言", "wxx", "wit", "123456"}
    var book2 Books

    book2.titile = "Python"
    fmt.Println(book)
    fmt.Println(book2)

    //range

    s := [...]string{"test1", "test2", "test3"}

    for i, s_i := range s {
        fmt.Println(i,": ",s_i)
    }
    
}
