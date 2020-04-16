from socket import *

# 访问服务端需要的地址
server_addr = ('127.0.0.1', 8888)


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    while True:
        try:
            name = input("name:")
            age = input("age:")
            sex = input("sex:")
            score = input("score:")
            data = "%s %s %s %s" % (name, age, sex, score)
            udp_socket.sendto(data.encode(), server_addr)
        except KeyboardInterrupt:
            break
    udp_socket.close()


if __name__ == '__main__':
    main()

# def main():
#     udp_socket = socket(AF_INET, SOCK_DGRAM)
#
#     while True:
#         try:
#             # 具体做的事情
#             print("===================================================")
#             name = input("Name:")
#             age = input("Age:")
#             sex = input("Sex:")
#             score = input("Score:")
#             data = "%s %s %s %s"%(name,age,sex,score)
#             udp_socket.sendto(data.encode(),server_addr) # 学生信息发送
#         except KeyboardInterrupt:
#             break
#
#     udp_socket.close()
#
# main()
# socket_student = socket(AF_INET, SOCK_DGRAM)
# l = []
# student_addr = ("127.0.0.1", 8584)
# while True:
#     student_name = input(">>name:")
#     student_age = input(">>age:")
#     student_sex = input(">>sex:")
#     student_score = input(">>score:")
#     l.append((student_name, student_age,
#               student_sex, student_score))
#     for i in l[0]:
#         socket_student.sendto(i.encode(),student_addr)
#         l.clear()
# socket_student.close()
