# 使用import导入os模块
import os

# 使用import导入pdfplumber模块
import pdfplumber

# 使用import导入openpyxl模块
import openpyxl 

# TODO 创建一个新工作簿赋值给变量newWb
newWb = openpyxl.Workbook()

# TODO 将名为Sheet的默认工作表，赋值给aSheet变量
aSheet = newWb["Sheet"]

# TODO 将PDF文档路径 /Users/yequ/Desktop/yqms/来访学生统计表.pdf，赋值给变量path
path = r"d:\test\yqms\来访学生统计表.pdf"

# TODO 读取path中的pdf文件，并赋值给pdf
pdf = pdfplumber.open(path)

# TODO 获取pdf第一页信息列表，赋值给变量page
page = pdf.pages[0]

# TODO 提取页面中第一个表格,赋值给tableData
tableData = page.extract_tables()[0]

# TODO 遍历tableData中的每个元素
for row in tableData:
    # TODO 将每个元素中的数据添加到工作表中
    aSheet.append(row)
           
# TODO 在工作表aSheet中，将D1单元格的值设置为"照片"
aSheet["D1"].value = "照片"

# TODO 将学生照片这个文件夹的路径，赋值给filePath
filePath = r"d:\test\yqms\学生照片"

# TODO for循环遍历aSheet工作表的所有行和其对应的索引
for idx,row in enumerate(aSheet.rows,1):
    # TODO 获取第一列单元格的值赋值给变量name
    name = row[0].value
    # TODO 判断当name等于 姓名 时
    if name == "姓名":
        # TODO 使用continue跳过本次循环
        continue
    # TODO 根据照片命名规则, 利用格式化字符串生成照片文件名
    picname = f"{name}.png"
    # TODO 利用os.path.join()函数合并照片路径并赋值给photoPath
    photoPath = os.path.join(filePath,picname)
    # TODO 使用openpyxl.drawing.image.Image()生成一个图片对象赋值给变量image
    image = openpyxl.drawing.image.Image(photoPath)
    # TODO 将图片使用add_image()函数添加到D列对应的行中
    aSheet.add_image(image,f"D{idx}")
        
# TODO 将Excel文档保存至指定路径/Users/yequ/Desktop/yqms/来访学生统计表.xlsx
newWb.save(r"d:\test\yqms\来访学生统计表.xlsx")