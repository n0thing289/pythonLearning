import socket
# 1. 创建套接字
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 连接服务器
client.connect(("192.168.224.1", 8080))
# 3. 发送数据
client.send("我喜欢你".encode("utf-8")) # 不再需要写ip和端口,并且用send
# 4. 关闭套接字
client.close()