# 导入pandas模块，并简称为"pd"
import pandas as pd

# 使用read_csv函数，获取文件/Users/xinxin/grade.csv
grade = pd.read_csv('/Users/xinxin/grade.csv')

# TODO 计算这个班的数学平均分，取整后赋值给变量M_mean
M_mean = grade["数学"].mean().round()

# TODO 计算这个班的语文平均分，保留一位小数后，赋值给变量C_mean
C_mean = grade["语文"].mean().round(1)

# TODO 使用print()函数格式化输出"这个班级的数学平均分，取整后是{M_mean}"
print(f"这个班级的数学平均分，取整后是{M_mean}")

# TODO 使用print()函数格式化输出"这个班级的语文平均分，保留一位小数后是{C_mean}"
print(f"这个班级的语文平均分，保留一位小数后是{C_mean}")