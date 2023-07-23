# 导入pandas模块，并以"pd"为该模块的简写
import pandas as pd

# 使用read_csv()函数，获取文件"/Users/titanic/train.csv"，并赋值给df
df = pd.read_csv("/Users/titanic/train.csv")   
 
# 使用布尔索引、列索引和count()函数计算各船舱人数
# 使用for循环依次计算1、2、3船舱的情况
for i in [1,2,3]:
    # TODO 使用布尔索引、列索引和count()函数计算i船舱的总人数,并赋值给给Pclass
    Pclass = df[df["Pclass"]==i]["PassengerId"].count() 

    # TODO 使用布尔索引、列索引和count()函数计算i船舱的存活人数,并赋值给Pclass_Survived
    Pclass_Survived = df[(df["Pclass"]==i)&(df["Survived"]==1)]["PassengerId"].count()

    # TODO 使用公式Pclass_Survived/Pclass，计算i号船舱的存活率，并赋值给Survived_rate
    Survived_rate = round((Pclass_Survived/Pclass)*100,2)

    # TODO 使用print()格式化输出 f"{i}号船舱存活率是{Survived_rate}"
    print(f"{i}号船舱存活率是{Survived_rate}%")