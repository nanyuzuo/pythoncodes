# TODO 使用import导入os模块
import os

# TODO 使用import导入pdfplumber模块
import pdfplumber

# TODO 使用import导入openpyxl模块
import openpyxl

# TODO 创建一个新工作簿赋值给变量newWb
newWb = openpyxl.Workbook()

# TODO 将名为Sheet的默认工作表赋，值给sheet变量
sheet = newWb["Sheet"]

# TODO 将PDF文件夹路径 /Users/acheng/Desktop/银行账单，赋值给变量path
path = r"d:\test\银行账单"

# TODO 使用os.listdir()函数获取该路径下所有的文件名称，并赋值给变量allItems
allItems = os.listdir(path)

# TODO 使用for循环遍历allItems
for item in allItems:

    # TODO 使用os.path.join()函数拼接pdf文件路径，赋值给pdfPath
    pdfPath = os.path.join(path,item)

    # TODO 读取PDF文档，并赋值给pdf
    pdf = pdfplumber.open(pdfPath)

    # TODO 使用for循环遍历pdf页面列表
    for page in pdf.pages:

        # TODO 使用extract_tables()函数，提取页面中的所有表格
        # 并将第一个表格赋值给tableData
        tableData = page.extract_tables()[0]

        # TODO 遍历列表tableData
        for row in tableData:

            # TODO 将表格每一行的数据添加到工作表中
            sheet.append(row)

    # TODO 格式化输出XX提取完成
    print(f"{item}提取完成")

# TODO 将工作簿保存到路径 /Users/acheng/Desktop/账单合集.xlsx
newWb.save(r"d:\test\银行账单\账单合集.xlsx")