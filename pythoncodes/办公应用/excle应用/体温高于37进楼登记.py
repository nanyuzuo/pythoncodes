# TODO 导入openpyxl模块
 import openpyxl

# TODO 使用openpyxl.load_workbook()函数读取“进楼登记.xlsx”工作簿
# 赋值给变量wb
wb = openpyxl.load_workbook("进楼登记.xlsx")
# TODO 通过wb加中括号获取名为“体温表”的工作表对象，赋值给变量tempSheet
tempSheet = wb["体温表"]

# 定义一个变量名为feverList列表
feverList = []

# 遍历体温表的行数据
for rowData in tempSheet.rows:
    # TODO 遍历行数据中，取出第一列姓名和第二列温度列数据
    # 姓名赋值给变量name，温度赋值给变量temp
    name = rowData[0].value
    temp = rowData[1].value
    

    # 因为数据第一行是文字"测量体温"，所以要先在判断中排除
    if temp == "测量体温":
        continue

    # TODO 判断温度数据大于37时
    if temp > 37:
        # TODO 使用append函数将姓名添加到列表feverList
        feverList.append(name)

# TODO 使用print输出feverList列表
print(feverList)