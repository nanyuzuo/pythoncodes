# 使用import导入os模块
import os

# TODO 将文件路径/Users/project 赋值给变量itemsPath
itemsPath = "/Users/project"

# TODO 使用os.listdir()函数获取该路径下所有的文件，并赋值给变量allItems
allItems = os.listdir(itemsPath)

# TODO 使用for循环遍历所有文件夹
for filedir in allItems:

    # TODO 使用os.path.join()函数，拼接当前文件夹的路径
    dirpath = os.path.join(itemsPath,filedir)

    # TODO 使用os.listdir()函数获取该文件夹路径下所有的文件，并赋值给变量allDocuments
    allDocuments = os.listdir(dirpath)
    
    # TODO 使用格式化函数，将“开题报告_姓名.docx”赋值给变量document1
    document1 = (f"开题报告_{filedir}.docx")

    # TODO 使用格式化函数，将“中期报告_姓名.docx”赋值给变量document2
    document2 = (f"中期报告_{filedir}.docx")

    # TODO 使用格式化函数，将“任务书_姓名.docx”赋值给变量document3
    document3 = (f"任务书_{filedir}.docx")

    # TODO 使用格式化函数，将“指导记录表_姓名.docx”赋值给变量document4
    document4 = (f"指导记录表_{filedir}.docx") 

    # TODO 判断该文件夹内，是否缺失document1这个文件
    if  document1 not in allDocuments:

        # TODO 如果缺失，使用格式化输出“xxx没有交开题报告”
        print(f"{filedir}没有交开题报告")

    # TODO 判断该文件夹内，是否缺失document2这个文件
    if  document2 not in allDocuments:

        # TODO 如果缺失，使用格式化输出“xxx没有交中期报告”
        print(f"{filedir}没有交中期报告")

    # TODO 判断该文件夹内，是否缺失document3这个文件
    if  document3 not in allDocuments:

        # TODO 如果缺失，使用格式化输出“xxx没有交任务书”
        print(f"{filedir}没有交任务书")

    # TODO 判断该文件夹内，是否缺失document4这个文件
    if  document4 not in allDocuments:

        # TODO 如果缺失，使用格式化输出“xxx没有交指导记录表”
        print(f"{filedir}没有交指导记录表")