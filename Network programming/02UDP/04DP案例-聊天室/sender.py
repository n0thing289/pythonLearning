import socket
import time


class Sender:
    def __init__(self, dest_ip, dest_port):
        # 创建套接字
        self.s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        # 初始化目标ip和端口
        self.dest_address = (dest_ip, dest_port)


    def send(self, contains):
        #发送数据
        self.s.sendto(contains.encode("utf-8"), self.dest_address)



if __name__ == "__main__":
    sender = Sender("10.208.96.42", 8081)
    str = input("请输入你想发送的数据: ")
    while True:
        time.sleep(1)
        sender.send("hi")