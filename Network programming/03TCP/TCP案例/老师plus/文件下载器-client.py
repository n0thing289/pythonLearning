import socket

# 1. 创建套接字
client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 连接tcp
HOST_NAME = (input("请输入服务器ip"), 10086)
client_s.connect(HOST_NAME)
print("连接服务器(%s)成功! " % HOST_NAME[0])

# 3. 获取要下载的文件名
download_filename = input("filename: ")

# 4. 将文件名发送给tcp服务期
client_s.send(download_filename.encode("utf-8"))

# 5. 接受文件的数据
respond = client_s.recv(1024 * 5000)
print("接受的数据如下:")
print(respond)
# # 6. 将数据存储到一个新的文件中
# with open(download_filename, "w") as f:
#     f.write(respond.decode("utf-8"))
#     print("下载文件(%s)成功" % download_filename)

# 6. 将数据存储到一个新的文件中
with open(download_filename, "wb") as f:
    f.write(respond)
    print("下载文件(%s)成功" % download_filename)

# 7. 关闭文件/套接字
client_s.close()
