import pymysql
import re

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")
cur = db.cursor()
f = open("dict.txt", "r")
l = []
for i in f:
    m = re.search(r"\w+\s", i).group()
    k = i.replace(m, " ").lstrip()
    l.append((m, k))

sql = "insert into words (word,mean) values (%s,%s);"
try:
    cur.executemany(sql, l)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
cur.close()
db.close()