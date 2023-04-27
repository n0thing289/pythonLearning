import socket
# 1
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 2
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

# 3

dest_info = ("<broadcast>", 2425)
send_content = "hi"
s.sendto(send_content.encode("utf-8"), dest_info)

# 4.
s.close()