'''
tcp客户端实现流程
'''
from socket import *

# 创建套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)
# 绑定地址
tcp_socket.bind(("192.168.40.130", 8888))

# 将套接字设置为监听套接字，监听
tcp_socket.listen(5)

print("wait:")
# 等待客户端回应
connect_socket, addr = tcp_socket.accept()
print("链接了", addr, "客户端")
while True:
    # 接收消息
    data = connect_socket.recv(20)
    if data.decode() == "##":
        break
    print("get:", data.decode())
    n = connect_socket.send(b'thanks')
    print("发送了%d bytes" % n)

# 关闭套接字
connect_socket.close()
tcp_socket.close()
