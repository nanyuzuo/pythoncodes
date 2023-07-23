# 导入模块
import pandas as pd

# 读取路径"/Users/clean/视频会员订单数据源.csv"的文件
df = pd.read_csv("/Users/clean/视频会员订单数据源.csv")

# 商品价格price，单位分转化成元
df['price'] = df['price'] /100

# 订单创建时间create_time和支付时间pay_time，转化成时间格式
df['create_time'] = pd.to_datetime(df['create_time'])
df['pay_time'] = pd.to_datetime(df['pay_time'])


# 处理缺失值

# 删除payment_provider这一列缺失值的行
dfPayNull = df[df['payment_provider'].isnull()]
df.drop(index=dfPayNull.index, inplace = True)

# 删除platform这一列缺失值的行
dfPlatNull = df[df['platform'].isnull()]
df.drop(index=dfPlatNull.index,inplace = True)


# 处理异常值

# TODO 删除price这一列不是25.00，68.00，248.00的异常值
df.drop(index=df[~df["price"].isin([25.00,68.00,248.00])].index,inplace=True)


# TODO 删除支付时间pay_time小于创建时间create_time的异常值

df.drop(index=df[df["pay_time"]<df["create_time"]].index,inplace=True)


# 处理重复值

# TODO 删除order_id这一列的重复值

df.drop(index=df[df["order_id"].duplicated()].index,inplace=True)

# 使用info函数，快速浏览数据集
df.info()