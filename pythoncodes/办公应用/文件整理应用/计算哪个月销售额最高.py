# 导入openpyxl模块
import openpyxl

# 将计算单月销售额的步骤移到函数getMonthlySold中
# 获取单月“火龙果可乐”销售额的函数
# 参数 filePath: 销售数据Excel文件路径
# 返回值: 计算出的销售额结果
def getMonthlySold(filePath):
    # 使用openpyxl.load_workbook()函数读取工作簿，文件路径使用函数参数filePath
    # 添加data_only=True打开工作簿，获取公式计算后的值
    wb = openpyxl.load_workbook(filePath, data_only=True)

    # 通过工作簿对象wb获取名为“销售订单数据”的工作表对象，并赋值给变量orderSheet
    orderSheet = wb["销售订单数据"]

    # 定义一个变量colaSold用来表示本月“火龙果可乐”的销售金额
    colaSold = 0

    # 遍历工作表的所有行数据
    for rowData in orderSheet.rows:
        # 商品名C列是第3列，索引也就是2
        productName = rowData[2].value
        # 获取订单总价I列的索引和总价
        priceIndex = openpyxl.utils.cell.column_index_from_string("I") - 1
        price = rowData[priceIndex].value
        
        # 判断如果productName是“火龙果可乐”
        if productName == "火龙果可乐":
            # 逐个添加总价到本月销售额(colaSold)里
            colaSold = colaSold + price
    
    # 将计算后的销售额colaSold返回
    return colaSold

# 定义一个空列表soldList来逐个装入各个月份的销售额
soldList = []

# 使用for循环和range，逐个遍历1~12的数字
# 注意：range的第二个参数是不包括到循环内的
for month in range(1,13):
    # 利用格式化字符串拼接Excel文件名，传入到获取单月销售额的函数并赋值给变量monthlySold
    monthlySold = getMonthlySold(f"2019年{month}月销售订单.xlsx")
    # 将“火龙果可乐”单月销售额monthlySold使用append函数逐个添加到列表中
    soldList.append(monthlySold)

# 使用max()函数获取最大的销售额并赋值给变量maxSold
maxSold = max(soldList)

# TODO 使用index()函数获取最大值的索引，索引值加1后得到月份赋值给maxMonth
maxMonth = soldList.index(maxSold) + 1
# TODO 输出最终的结果：火龙果可乐在{maxMonth}月份卖得最好
print(f"火龙果可乐在{maxMonth}月份卖得最好")