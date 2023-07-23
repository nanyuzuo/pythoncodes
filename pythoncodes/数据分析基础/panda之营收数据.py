# 导入pandas模块，并简称为"pd"
import pandas as pd

# 使用read_csv函数，获取文件/Users/xiaoxin/公司营收.csv
data = pd.read_csv('/Users/xiaoxin/公司营收.csv')

# TODO 使用.astype()函数将四个季度的营收数据更新为浮点数类型
data[['Q1','Q2','Q3','Q4']] = data[['Q1','Q2','Q3','Q4']].astype(float)

# TODO 添加新列”total“，数值为四个季度营收的和
data["total"] = data["Q1"] + data["Q2"] + data["Q3"] + data["Q4"]

# TODO 使用.max()函数将'total'这一新列的最大值输出
print(data["total"].max())

# TODO 使用.median()将'total'这一新列的中位数输出
print(data["total"].median())