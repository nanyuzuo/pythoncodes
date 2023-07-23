# 导入pandas模块，简称为pd
import pandas as pd

# 读取路径为"/Users/clean/视频会员订单数据源.csv"的文件，赋值给变量df
df = pd.read_csv("/Users/clean/视频会员订单数据源.csv")

# 商品价格price，单位分转化成元
df['price'] = df['price'] /100

# 使用to_datetime()函数，将订单创建时间create_time和支付时间pay_time，转化成时间格式
df['create_time'] = pd.to_datetime(df['create_time'])
df['pay_time'] = pd.to_datetime(df['pay_time'])

# TODO 使用fillna()函数，用"unknown"填充platform的缺失值
df["platform"].fillna("unknow",inplace=True)

# 输出df.info()
df.info()