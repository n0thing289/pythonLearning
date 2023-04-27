import socket


class QQ:
    # 初始化
    def __init__(self):
        # 创建套接字
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 绑定自身ip和自身端口套接字
        try:
            self.address = ("", 8081)
        except:
            print("端口被占用")
        self.s.bind(self.address)
    #发送
    def send(self):
        #1. 让用户输入要发送的数据
        msg = input("请输入要发送的数据: ")

        #2. 让用户指定目标ip,和目标端口
        dest_ip = input("请输入对方的ip地址:")
        dest_port = int(input("请输入对方的端口号:"))

        #3. 调用sendto()
        self.s.sendto(msg.encode("utf-8"), (dest_ip,dest_port))
        pass

    #接收
    def receive(self):
        recv_msg, recv_info = self.s.recvfrom(1024)
        print(">>>%s:%s" % (recv_info, recv_msg.decode("utf-8")))
        pass

    #菜单
    def main(self):
        while True:
            chose = input("======================" + "\n" +
                          "1. 发送消息" + "\n" +
                          "2. 接收消息" + "\n" +
                          "======================" + "\n" +
                          "请选择功能(-1退出): ")

            if chose == "1":
                self.send()
            elif chose == "2":
                self.receive()
            elif chose == "-1":
                print("程序退出~")
                self.s.close()
                break
            else:
                print("输入有误,请重新输入")

if __name__ == "__main__":
    qq = QQ()
    qq.main()

"""
    新的需求,我觉得每次都要写ip和目标端口很麻烦,因此我想写个好友的功能
    用字典  姓名:目标的ip
    1. 一开始可以让用户新建联系人
    2. 用户输入 姓名和ip
"""