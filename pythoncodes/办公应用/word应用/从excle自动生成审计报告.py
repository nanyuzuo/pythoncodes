# 导入openpyxl模块
import openpyxl

# 导入docx
import docx

# 添加data_only = True，读取工作目录里名为"年报.xlsx"的工作簿并赋值给变量wb
wb = openpyxl.load_workbook("年报.xlsx",data_only= True)

# 读取工作目录下名为"年报.docx"并赋值给变量doc
doc = docx.Document("年报.docx")

# TODO 使用enumerate()函数，遍历wb对象worksheets属性的所有变量（ws）和所属索引（index）
for index,ws in enumerate(wb.worksheets):

    # TODO 使用enumerate函数，遍历所有的行（row）和所属行数索引（rowNum）
    for rowNum,row in enumerate(ws.rows):

        # TODO 使用enumerate函数，遍历row对象的所有的单元格（cell）和所属列数索引（columnNum）       
        for columnNum,cell in enumerate(row):
            
            # TODO 变量cell使用.value属性，赋值给变量info
            info = cell.value

            # 判断如果info的数据类型是整型int的话
            if type(info) == int:

                # 判断如果info是负数的话
                if info < 0 :

                    # TODO 使用abs()函数，取info的绝对值，重新赋值给info
                    info = abs(info)

                    # TODO info使用格式化千位符，重新赋值给info
                    info = f"{info:,}"

                    # TODO info使用格式化两头加括号，重新赋值给info
                    info = f"({info})"

                # 判断如果info不为负数的话
                else:

                    # TODO info使用格式化千位符，重新赋值给变量info
                    info = f"{info:,}"
            
            # 如果info的数据类型不为整型int，那么变量info不做处理
            else:
            # TODO 判断如果变量info的值是None的话
                if info == None:

                # TODO 使用continue跳过
                    continue

            # TODO 将变量info，赋值给Word文档
            # 第index个表格的第rowNum行第columnNum列的单元格
            # 单元格的第1个段落第1个样式块的文本
            doc.tables[index].cell(rowNum,columnNum).text = info

# 完成循环修改后，生成一个在工作目录下的Word文档"年报_改.docx"
doc.save("年报_改.docx")

# 如果运行成功，输出success
print("success")