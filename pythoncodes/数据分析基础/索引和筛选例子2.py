# 导入pandas模块，并以"pd"为该模块的简写
import pandas as pd

# 使用pd.read_csv()函数
# 读取路径为 "/Users/find/信用卡用户信息.csv" 的CSV文件
# 并将结果赋值给变量data
data = pd.read_csv("/Users/find/信用卡用户信息.csv")

# TODO 使用.iloc索引输出数据中的前3行
print(data.iloc[:3])

# TODO 使用.iloc索引输出数据中的第2行，第3列的元素
print(data.iloc[1,2])

# TODO 将"credit_limit"中的数据除以10000，使其单位变为万
data["credit_limit"] = data["credit_limit"]/10000

# TODO 使用print()输出data变量中"credit_limit"列的数据
print(data["credit_limit"])