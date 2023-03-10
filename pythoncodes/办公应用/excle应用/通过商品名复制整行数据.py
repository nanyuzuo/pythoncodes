# TODO 使用import导入openpyxl模块
import openpyxl

# TODO 使用import导入os模块
import os

# TODO 将销售订单路径 "/Users/zhener/doc" 赋值给path
path = "/Users/zhener/doc"

# TODO 使用os.listdir()获取文件中的所有文件名，赋值给fileNames
fileNames = os.listdir(path)

# TODO for循环遍历列表中的所有文件名
for file in fileNames:

    # TODO 使用os.path.join()函数拼接文件路径，赋值给filePath
    filePath = os.path.join(path,file)

    # TODO 添加data_only=True，使用openpyxl.load_workbook()打开文档赋值给wb
    wb = openpyxl.load_workbook(filePath,data_only=True)

    # TODO 将文档中的 "销售订单数据" 工作表赋值给 orderSheet
    orderSheet = wb["销售订单数据"]

    
    # TODO 循环遍历orderSheet工作表的 .rows属性
    for row in orderSheet.rows:

        # TODO 将第3列商品名称的值赋值给productName
        productName = row[2].value

        # TODO 使用if判断productName等于"商品名"时就跳过
        if productName == "商品名":
            continue

        # TODO 使用wb打开名称为productName的工作表，并赋值给productSheet
        productSheet = wb[productName]
        
        # TODO 定义一个存放整行数据的空列表rowValues
        rowValues = []

        # TODO 使用for循环遍历该行row中的单元格
        for cell in row:
            
            # TODO 使用append()将单元格的值追加到列表rowValues中
            rowValues.append(cell.value)

        # TODO 利用append()函数将整行商品信息rowValues追加productSheet工作表中
        productSheet.append(rowValues)
        
    # TODO 将修改后的销售订单保存到原路径filePath
    wb.save(filePath)
