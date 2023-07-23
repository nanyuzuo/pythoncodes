# 导入pandas，并使用"pd"作为该模块的简写
import pandas as pd

# 使用read_csv()函数，获取文件"/Users/count/住户信息.csv"，并赋值给data
data = pd.read_csv("/Users/count/住户信息.csv")

# TODO 使用astype()函数，将data["身份证号"]转换为str类型
data["身份证号"] = data["身份证号"].astype(str)

# 创建储存性别的空列表gender
gender = []

# TODO 使用for循环遍历data["身份证号"]
for idNo in data["身份证号"]:
    
    # TODO 将身份证号的第13位([12])转换为int，并赋值给num
    num = int(idNo[12])

    # TODO 如果num是奇数
    if num % 2 ==1:

        # TODO 在gender列表中添加"男"
        gender.append("男")

    # TODO 如果num是偶数
    else:

        # TODO 在gender数组中添加"女"
        gender.append("女")

# TODO 将gender赋值给data["性别"]
data["性别"] = gender

# TODO 使用print()输出data
print(data)