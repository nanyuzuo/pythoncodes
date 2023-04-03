# 导入pymysql模块
import pymysql

# TODO 创建一个连接并存储在 conn 中，并使以下配置传递参数
conn = pymysql.connect(
    # TODO 服务器地址为 127.0.0.1
    host = '127.0.0.1',
    # TODO 端口号为 3306
    port = 3306,
    # TODO 用户名为 root
    user = 'root',
    # TODO 密码为 123456
    password = 'Ubuntu12.04',
    # TODO 数据库名为 nocturneshop
    database = 'nocturneshop')
    
# 创建游标对象
cur = conn.cursor()

# 存储SQL指令
SQL = '''
SELECT *
FROM brand;
'''

# 执行SQL语句
ret = cur.execute(SQL) 
print(f"本次查询共获得了{ret}条信息") 


# 获取一条数据
data = cur.fetchone() 
print(data)

# 接着获取4条数据
data = cur.fetchmany(4) 
print(data)

# 获取剩下所有数据
data_set= cur.fetchall() 
print(data_set)

# 关闭游标
cur.close()

# TODO 关闭连接
conn.close()