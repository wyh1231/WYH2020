import pymysql
import re

# 连接数据库

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")

# 生成游标对象cursor(操作数据库,执行sql语句,获取结果)
cur = db.cursor()

file = open("dict.txt","r")
f = file.readlines()
args_list = []
for line in f:
    l = re.findall(r"(\w+)\s+(.*)",line)
    args_list.extend(l)
sql = "insert into words(word,mean) values(%s,%s);"
try:
    cur.executemany(sql,args_list)
    db.commit()
except Exception:
    db.rollback()

# 关闭游标和数据库连接
cur.close()
db.close()