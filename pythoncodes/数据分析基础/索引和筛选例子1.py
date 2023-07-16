# 导入pandas模块，并简称为"pd"
import pandas as pd

# TODO 使用pd.read_csv()函数,读取路径为 "Users/NBA/NBA球员年薪数据.csv" 的CSV文件
# 使用参数index_col，将“id”这一列设置为索引
# 并将结果赋值给变量NBA_data
NBA_data = pd.read_csv("Users/NBA/NBA球员年薪数据.csv",index_col="id")

# TODO 使用.loc索引输出数据中的前3行
print(NBA_data.loc[10000:10002])

# TODO 使用.loc索引输出数据中的第1行和第3行
print(NBA_data.loc[[10000,10002]])