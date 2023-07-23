import pandas as pd
df = pd.read_csv("/Users/feifei/hotpot.csv")
# 计算性价比评分，通过赋值，将结果添加为df的"性价比评分"列
df["性价比评分"] = (df["口味评分"]/df["人均消费"])*40
# 计算氛围评分，通过赋值，将结果添加为df的"氛围评分"列
df["氛围评分"] = (df["服务评分"]+df["环境评分"])/2
#  使用round()函数对2个新列保留2位小数
df[["性价比评分","氛围评分"]] = df[["性价比评分","氛围评分"]].round(2)

# TODO 使用sort_values()对df的列"性价比评分"进行降序排序，并赋值给df_1
df_1 = df.sort_values(by="性价比评分",ascending=False)
# TODO 使用多列索引的方式，访问df_1的"店铺名称"和"性价比评分"2列，并赋值给df_ratio
df_ratio = df_1[["店铺名称","性价比评分"]]

# 使用print()输出df_ratio
print(df_ratio)