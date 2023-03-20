# TODO 使用import导入pdfplumber模块
import pdfplumber

# TODO 使用import导入docx模块
import docx

# TODO 将PDF文档路径/Users/yequ/Desktop/nameList/名单.pdf，赋值给变量path
path = r"d:\test\nameList\名单.pdf"

# TODO 读取pdfPath中的文件，并赋值给pdf
pdf = pdfplumber.open(path)

# TODO 新建一个空列表nameList
nameList = []

# TODO 遍历PDF文档获取每一页信息
for page in pdf.pages:

    # TODO 提取页面中的第一个表格,赋值给tableData
    tableData = page.extract_tables()[0]

    # TODO 遍历列表tableData,第一项到最后一项
    for row in tableData:
        # TODO 判断第一行中的元素等于 姓名 时
        if row[0] == "姓名":      
            # TODO 使用continue跳过本次循环
            continue            
        # TODO 把每一行的第一个元素（教师姓名），添加进nameList中
        nameList.append(row[0])

# TODO 读取Word文档/Users/yequ/Desktop/nameList/优秀教师.docx，赋值给变量doc
doc = docx.Document(r"d:\test\nameList\优秀教师.docx")

# TODO 以空格连接元素，将列表转换成字符串，赋值给newList
newList = " ".join(nameList)

# TODO 输出newList
print(newList)

# TODO 将newList作为段落添加进Word文档
doc.add_paragraph(newList)

# TODO 保存Word文档到/Users/yequ/Desktop/nameList/优秀教师.docx
doc.save(r"d:\test\nameList\优秀教师.docx")