# TODO 导入openpyxl模块
import openpyxl
# TODO 使用openpyxl.load_workbook()函数读取工作目录里名为"2019年10月销售订单.xlsx"的工作簿并赋值给变量wb 
# 记得添加data_only=True参数打开工作簿，获取公式计算后的值
wb = openpyxl.load_workbook("2019年10月销售订单.xlsx",data_only = True)

# TODO 通过工作簿对象wb获取名为“销售订单数据”的工作表对象，并赋值给变量orderSheet
orderSheet = wb["销售订单数据"]

# 定义一个变量chipsSold用来表示本月“榴莲味薯片”的销售金额
chipsSold = 0

# 遍历工作表的所有行数据
for rowData in orderSheet.rows:
    # TODO 获取这一行的商品名赋值给变量productName
    # 商品名C列是第3列，索引也就是2，记得添加.value读取单元格的值
    productName = rowData[2].value
    # 获取订单总价I列的索引
    priceIndex = openpyxl.utils.cell.column_index_from_string("I") - 1
    # TODO 根据索引获取本行订单总价并赋值给变量price
    price = rowData[priceIndex].value
    
    # TODO 判断productName是否是“榴莲味薯片”，如果是，就逐个添加到本月销售额(chipsSold)里
    if productName == "榴莲味薯片":
        chipsSold = chipsSold + price

# TODO 打印出本月销售额，格式为：2019年10月榴莲味薯片销售额为{销售总额}元
print(f"2019年10月{productName}销售额为{chipsSold}元")