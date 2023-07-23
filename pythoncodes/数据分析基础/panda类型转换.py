# 导入模块
import pandas as pd

# 读取文件
df = pd.read_csv("/Users/find/信用卡用户信息.csv")

# 输出phone_number这一列的数据类型
print(df["phone_number"].dtype)

# TODO 使用astype()，将phone_number这一列转化为字符串类型，重新赋值给phone_number这一列
df["phone_number"] = df["phone_number"].astype(str)

# 再输出phone_number这一列现在的数据类型
print(df["phone_number"].dtype)