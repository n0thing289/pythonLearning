import socket
'''
1. 创建套接字
2. 连接服务器
3. 发送数据
4. 关闭套接字
'''


class FileShareClient:
    """
    1. 创建TCP套接字
    2. 连接tcp服务器
    3. 发送请求的文件名
    4. 接受服务器传送的数据
    5. 创建新文件,数据持久化
    """
    def __init__(self):
        # 1. 创建套接字
        self.fsc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2. 连接服务器套接字
        self.TCP_ADDRESS = ()
        self.fsc.connect(self.TCP_ADDRESS)

    def send_filename(self):
        self.fsc.send(input("请输入需要请求的文件名称: ").encode("utf-8"))

    def receive_file(self):
        re_file = self.fsc.recv(1024 * 10)
        with open("re_file.jpg", "wb") as fp:
            fp.write(re_file)


if __name__ == "__main__":
    FSC = FileShareClient()
    FSC.send_filename()
    FSC.receive_file()