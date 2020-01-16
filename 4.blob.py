import pymysql

# 连接数据库

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")

# 生成游标对象cursor(操作数据库,执行sql语句,获取结果)
cur = db.cursor()

with open("timg.jpeg","rb") as f:
    data = f.read()
try:
    sql = "update cls set image=%s where name='Tina';"
    cur.execute(sql,[data])
    db.commit()
except Exception:
    db.rollback()


# 关闭游标和数据库连接
cur.close()
db.close()