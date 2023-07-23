# 导入pandas模块，简称为pd
import pandas as pd
# 使用read_csv()函数
# 读取路径"/Users/feifei/hotpot.csv"的文件，并赋值给变量df
df = pd.read_csv("/Users/feifei/hotpot.csv")

# TODO 使用列索引和str.contains()函数
# TODO 创建判断"店铺名称"列中的数据包含"牛"的判断条件，并赋值给变量beefpot
beefpot = df[df["店铺名称"].str.contains("牛")]

# TODO 将店铺名称设置为行索引，将新的Dataframe赋值给变量beefpot2
beefpot2 = beefpot.set_index("店铺名称")

# TODO 获取评分最高的行索引，也就是店铺名称
storename = beefpot2["口味评分"].idxmax()

# TODO 输出店铺名称
print(storename)

# 重置索引，还原dataframe
beefpot3 = beefpot2.reset_index()