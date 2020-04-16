from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
server_addr = ("192.168.40.130", 8888)
tcp_socket.connect(server_addr)
file_image = open("sjch.jpg", "rb")
while True:
    data = file_image.read(1024)
    if not data:
        tcp_socket.send(b"##")
        break
    tcp_socket.send(data)
tcp_socket.close()
