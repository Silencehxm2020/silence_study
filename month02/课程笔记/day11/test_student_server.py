from socket import *
import pymysql


class Database:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="123456",
                                  database="stu",
                                  charset="utf8")
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def insert_data(self, list_):
        sql = "insert into cls (name,age,sex,score) value (%s,%s,%s%s);"
        try:
            self.cur.execute(sql, list_)
            self.db.commit()
        except:
            self.db.rollback()

def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", 8888))
    db = Database()
    while True:
        try:
            data, addr = udp_socket.recvfrom(128)
            info = data.decode().split(" ")
            db.insert_data(info)
        except KeyboardInterrupt:
            break
    db.close()
    udp_socket.close()
    print("over")


if __name__ == '__main__':
    main()

# # 主函数启动程序
# def main():
#     udp_socket = socket(AF_INET, SOCK_DGRAM)  # 创建套接字
#     udp_socket.bind(("0.0.0.0", 8888))  # 绑定地址
#     db = Database()  # 实例化对象
#
#     while True:
#         try:
#             # 具体做的事情 data--> b"name age sex score"
#             data, addr = udp_socket.recvfrom(128)  # 接收学生信息
#             info = data.decode().split(' ') # info -->[name,age,sex,score]
#             db.insert_data(info)
#         except KeyboardInterrupt:
#             break
#
#     db.close()
#     udp_socket.close()
#     print("服务结束")
#
#
# main()


# ======================================================================================================
# db = pymysql.connect(host="localhost",
#                      port=3306,
#                      user="root",
#                      password="123456",
#                      database="books",
#                      charset="utf8")
# cur = db.cursor()
# socket_server = socket(AF_INET, SOCK_DGRAM)
# socket_server.bind(("127.0.0.1", 8584))
# l = []
# while True:
#     data, addr = socket_server.recvfrom(80)
#     print(data.decode())
#     l.append(data.decode())
#     if len(l) == 4:
#         sql = "insert into cls (name,age,sex,score) value (%s,%s,%s,%s);"
#         cur.execute(sql, l)
#         db.commit()
#         l.clear()
#
# cur.close()
# socket_server.close()
