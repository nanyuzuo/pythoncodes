# TODO 导入pandas模块，并以"pd"为该模块的简写
import pandas as pd

# TODO 使用read_csv()函数，获取文件"/Users/aliang/借贷用户信息表.csv"，并赋值给变量data
data = pd.read_csv("d:\\yequ\\data\\借贷用户信息表.csv")

# TODO 使用sample()函数，随机抽取样例10000个，并赋值给变量data
data = data.sample(10000)

# TODO 使用print()输出变量data
print(data)

# TODO 使用to_csv()函数，将data保存到指定路径"/Users/aliang/抽取样例信息表.csv"下
data.to_csv("d:\\yequ\\data\\抽取样例信息表.csv")