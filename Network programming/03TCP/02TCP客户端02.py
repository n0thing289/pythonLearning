import socket
"""感受建立连接的流程"""
# 1. 创建套接字
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 连接服务器
client.connect(("192.168.224.1", 8080))
# 3. 发送数据
send_contains = input("输入:")
client.send(send_contains.encode("gbk")) # 不再需要写ip和端口,并且用send

# 4. 接收数据
recv_msg = client.recv(1024)
print(recv_msg.decode("gbk"))# b'ni1' 说明是二进制的数据,只不过以正常方式显示
print(client.getsockname())# 拿到本机的ip和端口
# 5. 关闭套接字
client.close()

