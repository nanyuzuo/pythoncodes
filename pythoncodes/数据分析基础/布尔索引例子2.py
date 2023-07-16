# 导入pandas模块，简称为pd
import pandas as pd

# 使用pd.read_csv()函数读取路径为 "/Users/find/信用卡用户信息.csv" 的CSV文件，并将结果赋值给变量data
data = pd.read_csv("/Users/find/信用卡用户信息.csv")

# TODO 使用布尔索引
# 筛选出"sex"列中的数据等于"F",且"career"列中的数据等于"其他"的行数据
# 赋值给变量result
result = data[(data["sex"]=="F")&(data["career"]=="其他")]

# 使用print()输出结果
print(result)