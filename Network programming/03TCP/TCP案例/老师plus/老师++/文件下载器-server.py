import socket

# 1. 创建套接字
server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定套接字
ADDRESS = ("", 10086)
server_s.bind(ADDRESS)

# 3. 变为监听模式
server_s.listen(128)
print("正在等待客户端连接")

# 4. 等待连接
new_s, client_info = server_s.accept()
print("与客户端(%s)连接成功" % str(client_info))

# 5. 接受文件名数据
download_filename = new_s.recv(1024).decode("utf-8")
# # 6. 找到文件
# with open(download_filename, "r") as f:
#     content = f.read() # 读取的字符串类型
#
# # 7. 发送文件
# new_s.send(content.encode("utf-8")) # encode("xxx"),是把字符串编程二进制的数据

# 6. 找到文件
with open(download_filename, "rb") as f:
    content = f.read()  # 读取的是二进制,就是原本的存储形式

# 7. 发送文件
print(len(content))
new_s.send(str(len(content)).encode("utf-8"))
new_s.send(content)

# 8. 判断客户端再关闭套接字
new_s.close()
server_s.close()
