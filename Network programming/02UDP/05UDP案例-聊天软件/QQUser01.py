import socket


class QQ:
    # 初始化
    def __init__(self):
        # 创建套接字
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 尝试绑定自身ip和自身端口, 如果不行就再次给定端口再绑定
        try:
            self.address = ("", 7788)
            self.s.bind(self.address)
        except:
            new_port = int(input(
                "这台pc上 " + str(self.address[1]) + " 端口被占用" + "\n" +
                "请设置一个新的端口: "))
            self.address = ("", new_port)
            self.s.bind(self.address)

        # 定义一些存好友的变量
        self.friend_dictionary = {}

    # 发送
    def send(self):
        # # 1. 让用户输入要发送的数据
        # msg = input("请输入要发送的数据: ")
        #
        # # 2. 让用户指定目标ip,和目标端口
        # dest_ip = input("请输入对方的ip地址:")
        # dest_port = int(input("请输入对方的端口号:"))
        #
        # # 3. 调用sendto()
        # self.s.sendto(msg.encode("utf-8"), (dest_ip, dest_port))

        if len(self.friend_dictionary) == 0:
            print("请先添加好友")
            self.addDestination()

        # 1. 让用户输入要发什么
        send_msg = input("请输入要发送的数据: ")
        # 2. 根据谁,去查找ip
        dest_name = input("你要发给谁?: ")
        if dest_name not in self.friend_dictionary.keys():
            print("输入有误或者您未添加该好友")
            return
        self.s.sendto(send_msg.encode("utf-8"), self.friend_dictionary[dest_name])
        pass

    # 接收
    def receive(self):
        recv_msg, recv_info = self.s.recvfrom(1024)
        print(">>>%s:%s" % (recv_info, recv_msg.decode("utf-8")))
        pass

    # 菜单
    def main(self):
        while True:
            chose = input(
                "======================" + "\n" +
                "1. 发送消息" + "\n" +
                "2. 接收消息" + "\n" +
                "3. 新建好友联系方式" + "\n" +
                "4. 查看好友联系方式" + "\n" +
                "======================" + "\n" +
                "请选择功能(-1退出): ")

            if chose == "1":
                self.send()
            elif chose == "2":
                self.receive()
            elif chose == "3":
                self.addDestination()
            elif chose == "4":
                self.showFriends()
            elif chose == "-1":
                print("程序退出~")
                self.s.close()
                break
            else:
                print("输入有误,请重新输入")

    # 新建好友
    def addDestination(self):
        dest_userName = input("请输入好友的名子: ")
        dest_ip = input("请输入对方的ip: ")
        dest_port = input("请输入对方的port: ")
        self.friend_dictionary[dest_userName] = (dest_ip, int(dest_port))
        pass

    def showFriends(self):
        print(self.friend_dictionary)
        pass


qq = QQ()
qq.main()

"""
    新的需求,我觉得每次都要写ip和目标端口很麻烦,因此我想写个好友的功能
    用字典  姓名:(目标的ip, 目标的端口)
    一开始可以让用户新建联系人
"""
