import pymysql

# 连接一个数据库
# 下面2种连本机方式
# db = pymysql.connect(host='127.0.0.1', user='root', password='123456',database='test1db')
db = pymysql.connect(host='localhost', user='root', password='123456', database='bishe')
# 远程方式
# db = pymysql.Connect(host='10.36.151.86', user='root', password='123456',database='test1db')

# 创建一个游标
cur = db.cursor()

# sql语句
# sql = 'select version()'
i=1
for i in range(10):
    sql = "UPDATE bishe.sym SET 'Gender' = '1' WHERE 'id' = i"
    i=i+1
    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()
print('ok')
# 执行sql语句
# cursor.execute(sql)
#
# # 取一行结果
# result = cursor.fetchone()
#
# # 打印
# print(result)
