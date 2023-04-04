# 导入数据源
import tushare as ts
import openpyxl

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
    df = pro.trade_cal(exchange=exchange, start_date='20110101', end_date='20110110')
    # 将数据存储在data中
    data.append(df)
wb = openpyxl.Workbook()
ws = wb["Sheet"]

for df in data:
    # TODO 获取每一行数据
    for index,row in df.iterrows():
        # TODO 转换为列表
       row = list(row)
       ws.append(row)
wb.save(r"d:\test\stock.xlsx")
