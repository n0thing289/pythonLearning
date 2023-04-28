import socket
# 1. 创建套接字
server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定本地信息bind your ip and port
server_s.bind(("", 10086))

# 3. 将套接字默认的主动连接改为被动模式translate listen from
server_s.listen(128) # 随便写128 127
# 4. 等待客户端进行连接accept
new_s, client_info = server_s.accept()
print(client_info)
# 5. 接受/发送数据recv
while True:

    recv_content = new_s.recv(1024)
    if len(recv_content) == 0:
        break
    print(recv_content)
# 6. 关闭套接字
new_s.close()
server_s.close()


"""
    有哪些问题？
    1. 比客户端先调用close，会报错；正常应该时客户端先关闭，服务端后关闭
        怎么样？通过判断接收值，如果对方点了关闭，接受的是一个空值，没点关闭就一直等待接受
        
"""
