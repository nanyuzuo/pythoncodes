# 导入pandas模块，简称为pd
import pandas as pd

# 使用read_csv()函数读取路径为"/Users/rate/电脑评分.csv"，并赋值给变量df
df = pd.read_csv("/Users/rate/电脑评分.csv")

# TODO 使用drop()函数和布尔索引，将order_id这一列的缺失值删除
df.drop(index=df[df["order_id"].isnull()].index,inplace=True)

# TODO 使用for循环遍历["苹苹电脑","华华电脑","联联电脑","惠惠电脑","戴戴电脑","硕硕电脑"]
for i in ["苹苹电脑","华华电脑","联联电脑","惠惠电脑","戴戴电脑","硕硕电脑"]:
    
    # TODO 使用布尔索引筛选出brand等于i的数据，并赋值给df_i
    df_i = df[df["brand"]==i]
    
    # TODO 使用mean()函数求出rating列的均值
    mean_i = df_i["rating"].mean()
    
    # TODO 格式化输出i平均评分为mean_i
    print(f"{i}平均评分为{mean_i}")