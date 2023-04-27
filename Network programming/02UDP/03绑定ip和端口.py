import socket

#1. 创建一个UDP套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#2. 绑定一个ip和端口

# local_info = ("10.208.96.42", 8081)
local_info = ("", 10086)
s.bind(local_info)

#3. 发送数据
s.sendto("hello, world".encode("utf-8"), ("10.208.96.42",8080))  # encode()是把字符串转换成二进制比特

#4. 关闭套接字
s.close()