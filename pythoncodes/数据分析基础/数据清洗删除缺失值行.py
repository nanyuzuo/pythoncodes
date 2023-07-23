# 导入pandas模块，简称为pd
import pandas as pd

# 读取路径为"/Users/clean/视频会员订单数据源.csv"的文件，赋值给变量df
df = pd.read_csv("/Users/clean/视频会员订单数据源.csv")

# 商品价格price，单位分转化成元
df['price'] = df['price'] /100

# 使用to_datetime()函数，将订单创建时间create_time和支付时间pay_time，转化成时间格式
df['create_time'] = pd.to_datetime(df['create_time'])
df['pay_time'] = pd.to_datetime(df['pay_time'])

# 使用布尔索引和isnull函数，将payment_provider这一列的缺失值筛选出，赋值给变量dfPayNull
# dfPayNull就是，包含所有payment_provider这一列缺失值的行
dfPayNull = df[df['payment_provider'].isnull()]

# 使用drop函数，将包含所有payment_provider这一列缺失值的行删除
df.drop(index=dfPayNull.index, inplace = True)

# TODO 使用布尔索引和isnull函数，将platform这一列的缺失值筛选出，赋值给变量dfPlatNull
# dfPlatNull就是，包含所有platform这一列缺失值的行
dfPlatNull = df[df['platform'].isnull()]

# TODO 使用drop函数，将dfPlatNull，也就是包含所有platform这一列缺失值的行删除
df.drop(index=dfPlatNull.index,inplace = True)

# 使用df.info(),快速浏览数据集
df.info()