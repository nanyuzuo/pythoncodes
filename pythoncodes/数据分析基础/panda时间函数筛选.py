# 导入pandas模块
import pandas as pd
# 读取文件，并赋值给变量data
data = pd.read_csv("/Users/xingxing/兴兴药店2018年销售数据.csv")

# TODO 将data中"购药时间"这一列数据从字符串类型转换为日期类型
data["购药时间"] = pd.to_datetime(data["购药时间"])

# TODO 使用布尔索引，筛选出"购药时间"列中月份等于2的数据,并赋值给data_2018_2
data_2018_2 = data[data["购药时间"].dt.month == 2]

# 使用print()函数输出data_2018_2
print(data_2018_2)