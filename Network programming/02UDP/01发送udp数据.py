import socket

#1. 创建一个UDP套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#2. 发送数据
"""
    准备目标ip和目标端口的元组
"""
s.sendto("hello, world".encode("utf-8"),("10.208.96.86",8080))  # encode()是把字符串转换成二进制比特
#3. 关闭套接字

s.close()