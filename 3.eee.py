import pymysql

# 连接数据库

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")

# 生成游标对象cursor(操作数据库,执行sql语句,获取结果)
cur = db.cursor()

# 执行各种sql操作
sql = "insert into dict(word,mean) values (%s,%s);"
file = open("dict.txt","r")
while True:
    msg = file.readline()
    if not msg:
        break
    list_a = msg.split(" ",1)
    cur.execute(sql,list_a)
    db.commit()

# 关闭游标和数据库连接
cur.close()
db.close()
