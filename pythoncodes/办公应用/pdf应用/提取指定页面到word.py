# TODO 使用import导入pdfplumber模块
import pdfplumber

# TODO 使用import导入docx
import docx

# TODO 新建一个空白的word文档，赋值给file
file = docx.Document()

# TODO 将PDF文件夹路径/Users/yequ/Desktop/Translation/book.pdf，赋值给变量path
path = "/Users/yequ/Desktop/Translation/book.pdf"

# TODO 读取path中的文件，并赋值给pdf
pdf = pdfplumber.open(path)

# TODO 遍历数字2到9，作为页面索引
for num in range(2,10):

    # TODO 通过页面索引获取对应的页面列表，赋值给page
    page = pdf.pages[num]

    # TODO 提取页面中的文本,赋值给textData
    textData = page.extract_text()

    # TODO 将文本通过添加段落的方式添加到Word文档中
    file.add_paragraph(textData)

    # TODO 格式化输出 第X页提取完成
    print(f"第{num+1}页提取完成")

# TODO 保存文档到指定路径/Users/yequ/Desktop/book.docx
file.save("/Users/yequ/Desktop/book.docx")