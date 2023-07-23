# 导入pandas模块，并以"pd"为该模块的简写
import pandas as pd

# 使用pd.read_csv()函数读取路径为 "/Users/find/信用卡用户信息.csv" 的CSV文件，并将结果赋值给变量data
data = pd.read_csv("/Users/find/信用卡用户信息.csv")

# TODO 使用列索引和比较运算
# 创建判断"sex"列中的数据等于"F"的判断条件，并赋值给变量female
female = (data["sex"]=="F")

# TODO 使用列索引和比较运算
# 创建判断"career"列中的数据等于"其他"的判断条件，并赋值给变量other
other = (data["career"]=="其他")

# TODO 使用列索引和str.contains()函数
# 创建判断"address"列中的数据包含"四川"的判断条件，并赋值给变量city
city = (data["address"].str.contains("四川"))

# TODO 使用列索引和比较运算
# 创建判断"credit_limit"列中的数据超过100000的判断条件，并赋值给变量limit
limit = (data["credit_limit"]>100000)

# TODO 使用布尔索引和创建的判断条件
# 筛选出符合要求的数据，并赋值给变量result
result = data[female & other & city & limit]

# TODO 使用print()输出结果
print(result)