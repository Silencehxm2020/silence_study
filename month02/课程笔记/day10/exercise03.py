"""
soket 模块
"""
import socket

# 创建udp套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(udp_socket)

# 关闭套接字
udp_socket.close()
