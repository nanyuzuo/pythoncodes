# TODO 使用import导入os模块
import os

# TODO 使用import导入shutil模块
import shutil

# TODO 将文件路径/Users/project 赋值给变量itemPath
itemPath = "/Users/project"

# TODO 使用os.listdir()函数获取该路径下所有的文件，并赋值给变量allDocuments
allDocuments = os.listdir(itemPath)

# TODO 使用for循环遍历所有文件
for document in allDocuments:
    
    # TODO 使用os.path.splitext()函数获取文件名，赋值给变量documentName
    documentName = os.path.splitext(document)[0]

    # TODO 使用split()函数分割文件名，赋值给变量documentNameList
    documentNameList = documentName.split("_")

    # TODO 获取documentNameList的第2个元素，即文件归属的姓名，赋值给变量name
    name = documentNameList[1]

    # TODO 使用os.path.join()函数，将itemPath和document作为参数，拼接成当前文件的路径documentPath
    documentPath = os.path.join(itemPath,document)

    # TODO 使用os.path.join()函数，将itemPath和name作为参数，拼接成目标文件夹路径targetPath
    targetPath = os.path.join(itemPath,name)

    # TODO 使用os.path.exists()函数判断当如果目标文件夹targetPath不存在
    if not os.path.exists(targetPath):
        
        # TODO 使用os.mkdir()函数创建文件夹
        os.mkdir(targetPath)

    # TODO 使用shutil.move()函数移动文件，从documentPath到targetPath路径
    shutil.move(documentPath,targetPath)
