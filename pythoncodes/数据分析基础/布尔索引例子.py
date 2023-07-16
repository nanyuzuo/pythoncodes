# 导入pandas模块，并以"pd"为该模块的简写
import pandas as pd

# 使用read_csv()函数，获取文件"/Users/titanic/train.csv"，并赋值给df
df = pd.read_csv("/Users/titanic/train.csv")   

# TODO 使用for循环遍历1、2、3
for i in range(1,4):
    # TODO 使用布尔索引筛选出舱号为i的数据
    new_df = df[df["Pclass"]==i]    
    
    # TODO 在{}中添加变量，使用print()输出:第{i}号船舱的乘客信息是\n{new_df}
    print(f"第{i}号船舱的乘客信息是\n{new_df}")