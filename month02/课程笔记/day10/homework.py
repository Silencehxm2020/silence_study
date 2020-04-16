import pymysql
from socket import *

socket_server = socket(AF_INET, SOCK_DGRAM)
socket_server.bind(("127.0.0.1", 8884))

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")
cur = db.cursor()
while True:
    data, addr = socket_server.recvfrom(200)
    sql = "select mean from words where word=%s;"
    cur.execute(sql, (data.decode()))
    select_word = cur.fetchone()[0]

    socket_server.sendto(select_word.encode(), addr)
cur.close()
db.close()
socket_server.close()
