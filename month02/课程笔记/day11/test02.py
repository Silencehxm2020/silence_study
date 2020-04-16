from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)
server_addr = ("192.168.40.130", 8888)
# 发起链接
tcp_socket.connect(server_addr)
# 收发消息
while True:
    msg=input(">>")
    tcp_socket.send(msg.encode())
    if msg =="##":
        break
    data = tcp_socket.recv(20)
    print(data.decode())

tcp_socket.close()
