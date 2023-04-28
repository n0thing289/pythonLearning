import socket
import os
"""
1. 创建tcp套接字
2. 绑定套接字
3. 变为监听模式
4. 等待接受连接
5. 用新套接字接受数据
6. 判断对方关闭,再关闭
"""


class FileShareServer:
    def __init__(self):
        # 1. 创建套接字
        self.fss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # 2. 绑定套接字
        self.ADDRESS = ("", 10086)
        self.fss.bind(self.ADDRESS)
        # 3. 变为监听模式
        self.fss.listen(128)
        # 4. 等待连接
        self.new_fss, self.client_info = self.fss.accept()

    def receive_request(self):
        requested_filename = self.new_fss.recv(1024).decode("utf-8")
        return requested_filename

    def respond(self):
        # 1. 先去查找文件
        file_path = os.getcwd()
        files = os.listdir(file_path)
        file_index = files.index(self.receive_request())
        if file_index == -1:
            print("null file")
            pass
        file = files[file_index]
        # 2. 打开这个文件
        # 3. 发送这个文件
        with open(file, "rb") as fp:
            self.fss.send(fp)

        pass


if __name__ == "__main__":
    FSS = FileShareServer()
    while True:
        if FSS.new_fss != None:
            print(FSS.client_info, "客户端成功连接此服务器")

        # 1. 先接受客户端的请求文件名
        FSS.receive_request()
        # 2. 返回相应给客户端
        FSS.respond()