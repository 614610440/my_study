#coding:utf-8

import test_pb2

 # 解析
def parse(binary_msg):
    base_msg = test_pb2.BaseMsg()
    base_msg.ParseFromString(binary_msg)
    if base_msg.msgType == test_pb2.Test1MsgType :
        print ("This is Test1MsgType.")
        new_msg = test_pb2.Test1Msg()
        new_msg.ParseFromString(binary_msg)
        print (new_msg.name)
        print (new_msg.text)
    elif base_msg.msgType == test_pb2.Test2MsgType :
        print ("This is Test2MsgType.")
        new_msg = test_pb2.Test2Msg()
        new_msg.ParseFromString(binary_msg)
        print (new_msg.name)
        print (new_msg.pwd)
    else:
        print ("无法确认!")

def main():
    # 序列化
    test1_msg = test_pb2.Test1Msg()
    test1_msg.msgType = test_pb2.Test1MsgType

    test1_msg.name = "test1"
    test1_msg.text = "这是一个测试"
    msg1 = test1_msg.SerializeToString()

    test2_msg = test_pb2.Test2Msg()
    test2_msg.msgType = test_pb2.Test2MsgType

    test2_msg.name = "test2"
    test2_msg.pwd = "9999999"
    msg2 = test2_msg.SerializeToString()
    parse(msg1)
    parse(msg2)
    
if __name__ == '__main__':
    main()