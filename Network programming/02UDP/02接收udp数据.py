import socket

# 创建套接字
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 获取需要发送的数据
msg = input("请输入要发送的数据")

# 发送数据
s.sendto(msg.encode("ascii"), ("10.208.96.86", 8080))
s.sendto(msg.encode("ascii"), ("10.208.96.86", 8080))
s.sendto(msg.encode("ascii"), ("10.208.96.86", 8080))

# 接收数据并打印
recv_msg = s.recvfrom(1024)# 1. 参数是收集数据的最大值, 而且线程会卡在这里等待接收
print("%s(%d)>>>%s " % (recv_msg[1][0],recv_msg[1][1], recv_msg[0].decode("ascii")))# (b'http://www.cmsoft.cn', ('10.208.96.86', 8080)) 收到了内容(带b的都是二进制的数据)/来源的ip和端口

"""发的时候,要用编码, 收的时候要用解码; 同一件事，有不同记录方式"""
"""window的数据默认是gbk,windows发过来是gbk编码,那么解码要用gbk; 那个测试软件比较特殊, 显示界面使用utf-8解码,发送使用gbk默认编码"""
"""因为没有指定端口,所以发送时,端口一致在变化;接收方应该是固定端口的
    每次运行的时候,端口不变;否侧每次运行端口才不一样
"""
# 关闭套接字
s.close()