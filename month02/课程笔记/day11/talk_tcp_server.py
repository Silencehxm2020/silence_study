from socket import *
chat={"你好":"你好！"}
tcp_socket = socket(AF_INET, SOCK_STREAM)
server_addr = ("192.168.40.130", 8888)
tcp_socket.bind(server_addr)
tcp_socket.listen(5)
connect_socket, addr = tcp_socket.accept()
while True:
    data = connect_socket.recv(50).decode()

    if data == "##":
        break
    if data in chat:
        connect_socket.send(chat[data].encode())
    else:
        connect_socket.send("人家小".encode())
tcp_socket.close()
connect_socket.close()
