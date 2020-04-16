from socket import *

sockfd = socket(AF_INET, SOCK_DGRAM)
server_addr = ("127.0.0.1", 8884)
while True:
    msg=input(">>")
    if not msg:
        break
    sockfd.sendto(msg.encode(), server_addr)
    data, addr = sockfd.recvfrom(10000)
    print(data.decode())
sockfd.close()
