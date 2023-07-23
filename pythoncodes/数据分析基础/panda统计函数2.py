# 导入pandas，并使用"pd"作为该模块的简写
import pandas as pd

# 获取文件"/Users/book/bestsellers.csv"，并赋值给data
data = pd.read_csv("/Users/book/bestsellers.csv")

# TODO 使用列索引和max()函数，获取data["评分"]的最高评分，并赋值给maxScore
maxScore = data["评分"].max()

# TODO 使用布尔索引和maxScore获取所有拥有最高评分的数据，并赋值给maxData
maxData = data[data["评分"]==maxScore]

# TODO 使用列索引和min()函数，获取maxData["价格"]中的最低价格，并赋值给lowestPrice
lowestPrice = maxData["价格"].min()

# TODO 使用布尔索引和lowestPrice，获取maxData中价格最低的书籍信息，并赋值给result
result = maxData[maxData["价格"]==lowestPrice]

# 使用print()输出结果
print(result)