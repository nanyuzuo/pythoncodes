# TODO 导入pandas模块，并简称为"pd"
import pandas as pd

# TODO 依次定义字典info和列表continent
info = {'lifeExp':[54.8,73.6,70.7,77.6,80.7], 'gdpPercap':[3089,11003,12473,25054,29810]}
continent =['Africa','America','Asia','Europe','Oceania']


# TODO 使用pd.DataFrame()函数构造指定DataFrame
# 把字典info作为values和columns，列表continent作为index
# 将结果赋值给变量df
df = pd.DataFrame(info,index=continent)

# TODO 使用print()输出df
print(df)