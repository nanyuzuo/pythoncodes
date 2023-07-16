# TODO 导入pandas模块，并简称为"pd"
import pandas as pd

# TODO 依次定义year和count这两个列表
year = [1952,1957,1962,1967,1972]
count = [842,924,1026,1153,1307]

# TODO 使用pd.Series()函数构造指定Series
# 将count作为values，year作为index
# 把结果赋值给变量pop
pop = pd.Series(count,index=year)

# TODO 使用print()输出变量pop
print(pop)