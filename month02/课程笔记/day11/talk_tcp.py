from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
server_addr = ("192.168.40.130", 8888)
tcp_socket.connect(server_addr)
while True:
    msg = input(">>")
    tcp_socket.send(msg.encode())
    if msg == "##":
        break
    data=tcp_socket.recv(1024)
    print(data.decode())
tcp_socket.close()
