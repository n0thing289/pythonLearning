import socket
class Server:
    """主程序, 不断运行一直等待接收其他程序发过来的数据,收到数据就显示"""
    def __init__(self):
        #1. 创建套接字
        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #2. 绑定套接字(服务端)
        address = ("", 8081)
        self.s.bind(address)

    def main(self):
        while True:
            contains, client_info = self.s.recvfrom(1024)
            print("%s(%d)>>> %s" % (client_info[0],client_info[1],contains.decode("utf-8")))

if __name__ == "__main__":
    serve = Server()
    serve.main()
