import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="books",
                     charset="utf8")
cur = db.cursor()
# f = open("qingwa.jpg", "rb")
# data = f.read()
# try:
#     sql = "update cls set image=%s where name='Abby';"
#     cur.execute(sql, [data])
#     db.commit()
# except:
#     db.rollback()
sql = "select image from cls where name='Abby';"
cur.execute(sql)
data = cur.fetchone()
f = open('daqingwa.jpg', 'wb')
f.write(data[0])
f.close()
cur.close()
db.close()