# TODO 使用import导入os模块
import os

# TODO 使用import导入shutil模块
import shutil

# TODO 使用import导入openpyxl模块
import openpyxl

# TODO 使用openpyxl.load_workbook()函数读取"/Users/ahua/汇总.xlsx"路径下工作簿并赋值给变量wb
wb = openpyxl.load_workbook("/Users/ahua/汇总.xlsx")

# TODO 通过工作簿对象wb获取"面试教师名单"的工作表对象，并赋值给变量teSheet
teSheet = wb["面试教师名单"]

# TODO 将教师简历文件夹路径 "/Users/ahua/teacher" 赋值给变量path
path = "/Users/ahua/teacher"

# TODO 使用os.listdir()函数获取该路径下所有的文件(夹)，并赋值给变量allItems
allItems = os.listdir(path)

# TODO 使用for循环遍历所有文件(夹)
for item in allItems:
    
    # TODO 使用os.path.splitext()获取文件后缀名，赋值给extension
    extension = os.path.splitext(item)[1]

    # TODO 判断文件后缀名不是 .docx 时，就跳过
    if extension != ".docx":
        continue

    # TODO 使用os.path.splitext()获取文件名部分，也就是姓名和工作岗位，赋值给nameJob
    nameJob = os.path.splitext(item)[0]
    
    # TODO 使用split()函数分割"-"获取教师的名字，赋值给name
    name = nameJob.split("-")[0]

    # TODO 遍历 "面试教师名单" 工作表的.rows属性
    for row in teSheet.rows:

        # TODO 使用if判断每行第1个元素是教师的名字，与文件夹中的名字相等时
        if row[0].value == name:

            # TODO 找到每行第9个元素，下标为8的值，赋值给job
            job = row[8].value

            # TODO 使用os.path.join()函数拼接工作岗位文件夹路径，赋值给jobPath
            jobPath = os.path.join(path,job)

            # TODO 使用os.path.exists()判断目标文件夹不存在
            if not os.path.exists(jobPath):

                # TODO 使用os.mkdir()函数创建文件夹
                os.mkdir(jobPath)

            # TODO 使用os.path.join()函数拼接原文件路径，并赋值给变量oldPath
            oldPath = os.path.join(path,item)
                    
            # TODO 使用os.path.isdir()判断当oldPath路径不是文件夹时
            if not os.path.isdir(oldPath):

                # TODO 使用shutil.move()移动文件到分类文件夹去
                shutil.move(oldPath,jobPath)