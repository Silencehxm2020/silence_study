# import pymysql
from socket import *

#
#
# class Database:
#     def __init__(self):
#         self.db = pymysql.connect(host="localhost",
#                                   port=3306,
#                                   user="root",
#                                   password="123456",
#                                   database="books",
#                                   charset="utf8")
#         self.cur = self.db.cursor()
#
#     def insert_data(self, data):
#         try:
#             sql = "update cls set image=%s where name='Abby';"
#             self.cur.execute(sql, [data])
#             self.db.commit()
#         except:
#             self.db.rollback()


tcp_socket = socket(AF_INET, SOCK_STREAM)
server_addr = ("192.168.40.130", 8888)
tcp_socket.bind(server_addr)
tcp_socket.listen(5)
connect_socket, addr = tcp_socket.accept()
f = open("xiaoqingwa.jpg","wb")
while True:
    data = connect_socket.recv(2018)
    if data == b"##":
        break
    f.write(data)
f.close()
tcp_socket.close()
connect_socket.close()
