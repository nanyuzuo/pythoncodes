# TODO 放假通知是一份Word文档，家长们阅读签字后需将文件名改为"学生班级-学生姓名-端午节放假通知回执.docx"发回给班主任。
# TODO 班上一共有44名学生，所有学生的姓名都已经存储在了studentName列表中。
# TODO 没有交回执，需要先创建一个有全班同学姓名的工作簿，里面有一张工作表，名称为“七年级六班”，然后将这些未交回执的学生后面的单元格内标上“x”（小写字母x）

# TODO 使用import导入os模块
import os

# TODO 使用import导入openpyxl模块
import openpyxl

# 存储了全班学生的姓名列表studentName
studentName = ['吕婷婷', '肖槐', '魏皖怡', '胡轶轩', '包印雪', '谭彦', '周宇', '吴琪', '龚静雯', '张思思', '潘婷', '夏乐群', '朱佩玉', '隋胜男', '朱薇', '唐梅', '罗勇', '林贸然', '张丽', '张可馨', '汪洋', '韩明希', '杜宇琳', '胡连群', '岳海洋', '李雅梦', '蔡林芮', '孟轩', '项文彦', '苏培坤', '惠红', '顾洪彬', '卡欣', '陶振英', '子顺', '成洛', '邹德浩', '王思亮', '叶家有', '王德滋', '杨少帆', '谢福顺', '刘军', '李多钰']

# TODO 将回执的路径 /Users/qiao/回执 赋值给变量receiptPath
receiptPath = "/Users/qiao/回执"

# TODO 使用os.listdir()函数获取该路径下所有的回执，并赋值给变量allItems
allItems = os.listdir(receiptPath)

# 定义一个空列表变量submitList，用于存储已提交回执的学生姓名
submitList = []

# TODO 使用for循环遍历所有文件
for item in allItems:
    
    # TODO 使用split()函数以"-"分隔文件名，并赋值给变量result
    result = item.split("-")

    # TODO 获取result中的第2个元素【文件名中的学生姓名】，并使用append()函数将名字添加到submitList中
    submitList.append(result[1])

# TODO 使用openpyxl.Workbook()函数创建一个新的工作簿，并赋值给newWb
newWb = openpyxl.Workbook()

# TODO 将默认工作表Sheet赋值给变量aSheet
aSheet = newWb["Sheet"]

# TODO 将aSheet工作表名称修改为“七年级六班”
aSheet.title = "七年级六班"

# 定义一个变量rowNum，起始值为1，用于存储当前数据在表格中的行数（Excel表格中行数从“1”开始）
rowNum = 1

# TODO 使用for循环遍历全班同学姓名列表studentName
for name in studentName:

    # TODO 利用变量rowNum和格式化输出，逐个把studentName列表中的名字赋值到表格第一列的单元格中
    aSheet[f"A{rowNum}"].value = name

    # TODO 判断当前学生名字是否不在列表submitList【已交回执名单】中
    if name not in submitList:

        # TODO 若不在，利用变量rowNum和格式化输出，在对应第二列的单元格中填入"x"
        aSheet[f"B{rowNum}"] = "x"

    # 将变量rowNum加一，进入下一行中
    rowNum = rowNum + 1

# TODO 使用save()函数将工作簿保存到 /Users/qiao/回执/夜曲中学七年级六班回执提交情况.xlsx 路径下
newWb.save("/Users/qiao/回执/夜曲中学七年级六班回执提交情况.xlsx")