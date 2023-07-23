import pandas as pd
df = pd.read_csv("/Users/time/电商数据.csv" , usecols= [10])

# TODO 使用to_datetime函数，将pay_time这一列转化为时间类型，重新赋值给pay_time这一列
df["pay_time"] = pd.to_datetime(df["pay_time"])

# TODO 使用strftime函数，将pay_time这一列转化为"%Y年%m月%d日"的格式，赋值给date
date = df["pay_time"].dt.strftime("%Y年%m月%d日")

# TODO 使用strftime函数，将pay_time这一列转化为"星期%u"的格式，赋值给week
week = df["pay_time"].dt.strftime("星期%u")

# 输出date
print(date)
# 输出week
print(week)