
import pymysql

# 连接数据库

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")


cur = db.cursor()
name1 = input(">>")
sql = "select name,hobby,price from interest where name='%s'" % name1
cur.execute(sql)  # =%s      cur.execute(sql,[name1])

data = cur.fetchall()
print(data)
print(data)





# 关闭游标和数据库连接
cur.close()
db.close()

