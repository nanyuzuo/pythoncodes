# 导入模块
import pandas as pd
# 读取文件
data = pd.read_csv("/Users/aliang/抽取样例信息表.csv")

# TODO 使用fillna()函数，用"unknown"填充
# "上次还款日期"、"上次还款本金"和"上次还款利息"这三列的缺失值
data["上次还款日期"].fillna("unknown",inplace=True)
data["上次还款本金"].fillna("unknown",inplace=True)
data["上次还款利息"].fillna("unknown",inplace=True)

# TODO 使用布尔索引和isnull()函数
# 筛选出"下次计划还款日期"这一列的缺失值
# 并赋值给变量dfNull
dfNull = data[data["下次计划还款日期"].isnull()]

# TODO 使用drop函数，删除dfNull所对应的行数据
data.drop(index=dfNull.index,inplace=True)

# 输出data.info()
data.info()