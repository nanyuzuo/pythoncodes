# 导入pandas模块，简称为pd
import pandas as pd

# 使用read_csv()函数
# 读取路径"/Users/keyuan/ramenRatings.csv"的文件，并赋值给变量df
df = pd.read_csv("/Users/keyuan/ramenRatings.csv")

# TODO 将碗装拉面品牌数量、杯装拉面品牌数量和袋装拉面品牌数量相加,做为df的新列"count"
df["count"] = df["Bowl"] + df["Cup"] + df["Pack"]

# TODO 使用sort_values()函数
# 根据品牌数量总和，也就是"count"列，将原数据df降序排序，并赋值给df
df = df.sort_values(by="count",ascending=False)

# TODO# 使用head()访问df的前5行，并赋值给变量top_5
top5 = df.head()
# TODO 输出top_5
print(top5)