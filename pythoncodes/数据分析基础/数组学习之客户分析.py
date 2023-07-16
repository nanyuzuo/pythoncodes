# TODO 导入numpy
import numpy as np

# TODO 依次创建年龄和年收入对应的数组
ageArr = np.array([23,21,22,25,24])
incomeArr = np.array([154,114,145,132,198])


# TODO 依次计算年龄的平均值和年收入的平均值
ageAvg = ageArr.mean()
incomeAvg = incomeArr.mean()

# TODO 依次计算年龄的中位数和年收入的中位数
ageMed = np.median(ageArr)
incomeMed = np.median(incomeArr)


# TODO 根据公式，计算预期投入额
preIn = (ageMed+incomeMed) * 0.12

# TODO 根据题目要求，格式化输出结果
print(f"目标客户为21岁-25岁年龄段客户，平均年龄为{ageAvg}岁，平均年收入为{incomeAvg}K，年龄中位数为{ageMed}岁，年收入中位数为{incomeMed}K，预期投入额为{preIn}K")