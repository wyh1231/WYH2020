"""
    数据库读取
"""
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

# 执行各种sql操作
sql = "select name,age,score from cls;"
cur.execute(sql)  # 执行sql语句

# 获取结果方法1
# for item in cur:
#     print(item)

# 获取方法2
# one_row = cur.fetchone()  # 取一个
# print(one_row)

# many_row = cur.fetchmany(3)  # 获取多个
# print(many_row)

# 获取所有
all_row = cur.fetchall()
print(all_row)

# 关闭游标和数据库连接
cur.close()
db.close()