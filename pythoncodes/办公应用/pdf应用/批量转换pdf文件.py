# 使用import导入os模块
import os

# 使用import导入pdfplumber模块
import pdfplumber

# 使用import导入docx模块
import docx

# TODO 将桌面路径/Users/yequ/Desktop，赋值给desktopPath
desktopPath = "/Users/yequ/Desktop"

# TODO 使用os.path.join()函数拼接"稿件文档"文件夹路径，赋值给wordPath
wordPath = os.path.join(desktopPath,"稿件文档")

# TODO 判断如果桌面上没有这个文件夹，就新建一个
if not os.path.exists(wordPath):
    os.mkdir(wordPath)

# TODO 将PDF文件夹路径 /Users/yequ/Desktop/Python，赋值给变量path
path = "/Users/yequ/Desktop/Python"

# TODO 使用os.listdir()函数获取该路径下所有的文件名称，并赋值给变量allItems
allItems = os.listdir(path)

# TODO 使用for循环遍历allItems
for item in allItems:

    # TODO 分割文件名，获取文件名称，赋值给name
    name = os.path.splitext(item)[0]

    # TODO 使用os.path.join()函数拼接pdf文件路径，赋值给pdfPath
    pdfPath = os.path.join(path,item)

    # TODO 读取pdfPath中的文件，并赋值给pdf
    pdf = pdfplumber.open(pdfPath)

    # TODO 新建一个Word文档，赋值给file
    file = docx.Document()

    # TODO 使用for循环遍历pdf页面信息列表
    for page in pdf.pages:
        # TODO 提取页面中的文本,赋值给textData
        textData = page.extract_text()

        # TODO 在Word文档中添加替换后文本内容段落
        file.add_paragraph(textData)
    
    # TODO 给每个新生成的Word文档拼接docx后缀名，组成文件名，赋值给filename
    filename = name + ".docx"

    # TODO 使用os.path.join()函数拼接文件夹中Word文档的路径
    savePath = os.path.join(wordPath,filename)
    
    # TODO 保存文档
    file.save(savePath)

    # TODO 格式化输出 XX提取完成
    print(f"{filename}提取完成")