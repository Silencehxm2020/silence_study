"""
tcp 服务端实现流程
重点代码
"""

# from socket import *
#
# # 创建tcp套接字
# tcp_socket = socket(AF_INET,SOCK_STREAM)
#
# # 绑定地址
# tcp_socket.bind(("192.168.94.140",8888))
#
# # 将套接字设置为监听套接字,监听队列大小为5
# tcp_socket.listen(5)
#
# print("等待客户端链接....")
# # 等待处理客户端链接
# connect_socket,addr = tcp_socket.accept()
# print("链接了",addr,"客户端")  # 打印地址
#
# # 接收消息
# while True:
#     # 客户端退出,recv会返回空字节串
#     data = connect_socket.recv(5)
#     if not data:
#         break
#     print("接收到:",data.decode())
#     n = connect_socket.send(b'Thanks') # 发送字节串
#     print("发送了%d bytes"%n)
#
# # 关闭套接字
# connect_socket.close()
# tcp_socket.close()

from socket import *

# 穿件套接字
tcp_server = socket()
server_addr = ('127.0.0.1', 8888)
# 绑定地址
tcp_server.bind(server_addr)
# 监听
tcp_server.listen(5)
# 等待处理客户端链接
connec_socket, addr = tcp_server.accept()
#收发
while True:
    data = connec_socket.recv(20)
    # if data.decode() ="##"   #接收到指定字符后退出
    #     break
    if not data:  #客户端退出后退出
        break
    print(data.decode())
    connec_socket.send(b"thanks")
