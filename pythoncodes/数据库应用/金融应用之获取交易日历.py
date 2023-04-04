# 导入数据源
import tushare as ts

# 通过账号访问数据源
token = "0b99e2c05de16fec10076ebced34393706aa2bd6935c6629eeaf4637"
pro = ts.pro_api(token)

# 获取交易日历
# 参数分别为 交易所、开始日期、结束日期
stock_exchange = ['SSE', 'SZSE']
# 存储数据的列表
data = []
# 获取两个交易所的数据
for exchange in stock_exchange:
    df = pro.trade_cal(exchange=exchange, start_date='20110101', end_date='20201231')
    # 将数据存储在data中
    data.append(df)
print(data)

'''part 2'''
# 导入驱动
import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost', port = 3306, user='root', password='Ubuntu12.04', charset='utf8mb4')
# 创建游标
cur = conn.cursor()
# 创建数据库
SQL1 = '''
 CREATE DATABASE tushare charset='utf8mb4';
 '''
# 通过游标执行
cur.execute(SQL1)

# 选择数据库
SQL = '''
USE tushare;
'''
# 通过游标执行
cur.execute(SQL)

# 创建交易日历表
SQL2 = '''CREATE table trade_cal(
`exchange` varchar(100),
`cal_date` date,
`is_open` bit,
`pretrade_date` date
);'''

# 通过游标执行
cur.execute(SQL2)

'''part 3'''
# TODO 为表中插入数据
for df in data:
    # TODO 获取每一行数据
    for index,row in df.iterrows():
        # TODO 转换为列表
        row = list(row)
        # TODO 预留参数
        SQL3 = '''
              INSERT INTO trade_cal  (exchange,cal_date,is_open,pretrade_date) VALUES (%s,%s,%s,%s);
              '''
         
        # TODO 插入并传递参数
        cur.execute(SQL3,row)
       
        
# 提交
conn.commit()
# 关闭游标
cur.close()
# 关闭联结
conn.close()       