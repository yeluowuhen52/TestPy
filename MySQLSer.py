import pymysql
import json

# 连接数据库
connection = pymysql.connect(host='localhost', user='root', password='root', database='wechat_prod')

try:
    # 使用cursor()方法获取操作游标 
    with connection.cursor() as cursor:
        # 执行SQL查询
        cursor.execute(
            "SELECT id,code,name,ip,DATE_FORMAT(create_time, '%Y-%m-%d %H:%i:%s') as create_time ,DATE_FORMAT(update_time, '%Y-%m-%d %H:%i:%s') as update_time,state FROM pub_custom")

        # 获取所有记录列表
        rows = cursor.fetchall()

        # 使用json模块将结果序列化为JSON格式
        json_data = json.dumps([dict(zip(tuple(column[0] for column in cursor.description), row)) for row in rows])

        print(json_data)

finally:
    # 关闭数据库连接
    connection.close()
