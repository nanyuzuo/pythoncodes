import pymysql
import tushare as ts
import pandas as pd

# 通过账号访问数据源
token = "0b99e2c05de16fec10076ebced34393706aa2bd6935c6629eeaf4637"
pro = ts.pro_api(token)

# 获取数据
codes = ['000001.SH', '399001.SZ', '000016.SH', '000300.SH', '000905.SH']
df = []
for code in codes:
    data = pro.index_daily(ts_code=code, start_date='20110101', end_date='20201231', fields = ['ts_code', 'trade_date', 'close', 'open', 'high', 'low', 'pre_close', 'vol'])
    df.append(data)
df = pd.concat(df,ignore_index = True)

# 连接数据库
conn = pymysql.connect(host='localhost', port = 3306, user='root', password='Ubuntu12.04', database='tushare', charset='utf8')


cur = conn.cursor()

# 创建表格 comment 为表格的注释
SQL = '''
CREATE table tushare.index_daily(
`ts_code` varchar(100) comment '指数代码',
`trade_date` date comment '交易日期',
`open` float(255,5) comment '开盘价',
`high` float(255,5) comment '最高价',
`low` float(255,5) comment '最低价',
`close` float(255,5) comment '收盘价',
`pre_close` float(255,5) comment '昨收价',
`vol` float(255,5) comment '成交量 （手）'
);
'''
cur.execute(SQL)

# 插入数据
for index, row in df.iterrows():
    SQL = f'''
        INSERT INTO tushare.index_daily
         VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
        '''
    cur.execute(SQL, list(row))

# 提交数据
conn.commit()

# 关闭
cur.close()
conn.close()