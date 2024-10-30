# 导入第三方库
import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost', user='root', password='root', database='wechat_prod')


# 创建游标
cursor = conn.cursor()

# 执行SQL语句
cursor.execute("SELECT * FROM pub_custom")

# 获取查询结果
rows = cursor.fetchall()

for row in rows:
    print(row)
# 打印查询结果
# print(rows)

# 关闭游标和连接
cursor.close()
conn.close()

