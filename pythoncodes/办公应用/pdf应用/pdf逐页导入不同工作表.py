# TODO 使用import导入os模块
import os

# TODO 使用import导入pdfplumber模块
import pdfplumber

# TODO 使用import导入openpyxl模块
import openpyxl

# TODO 创建一个新工作簿，赋值给newWb
newWb = openpyxl.Workbook()

# TODO 将PDF文件夹路径 /Users/yequ/Desktop/bankBalance，赋值给变量path
path = "/Users/yequ/Desktop/bankBalance"

# TODO 使用os.listdir()函数获取该路径下所有的文件名称，并赋值给变量allItems
allItems = os.listdir(path)

# TODO 使用for循环遍历allItems
for item in allItems:
    
    # TODO 分割文件名，获取第一个元素文件名称，赋值给变量name
    name = os.path.splitext(item)[0]

    # TODO 以变量name为参数，新建工作表，赋值给newSheet
    newSheet = newWb.create_sheet(name)

    # TODO 使用os.path.join()函数拼接pdf文件路径，赋值给pdfPath
    pdfPath = os.path.join(path,item)

    # TODO 读取pdfPath中的文件，并赋值给pdf
    pdf = pdfplumber.open(pdfPath)

    # TODO 提取pdf第一页页面信息列表，赋值给page
    page = pdf.pages[0]

    # TODO 提取页面中的第一个表格，赋值给tableData
    tableData = page.extract_tables()[0]

    # TODO 遍历表格的每一行
    for row in tableData:

        # TODO 将每一行的数据添加到工作表中
        newSheet.append(row)

# TODO 将名为Sheet的默认工作表，赋值给aSheet变量
aSheet = newWb["Sheet"]

# TODO 删除默认工作表
newWb.remove(aSheet)

# TODO 将Excle文档保存至指定路径/Users/yequ/Desktop/年底合集.xlsx
newWb.save("/Users/yequ/Desktop/年底合集.xlsx")