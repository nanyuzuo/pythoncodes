# TODO 使用import导入os模块
import os

# TODO 使用import导入shutil模块
import shutil

# TODO 将文件夹路径/Users/yequ/Desktop/exam 赋值给变量path
path = "/Users/yequ/Desktop/exam"

# TODO 使用os.listdir()函数获取该路径下所有的文件(夹)，并赋值给变量allItems
allItems = os.listdir(path)

# TODO 使用for循环遍历所有文件(夹)
for file in allItems:
    # TODO 使用split()分割文件名，获取第一个元素，赋值给classInfo
    classInfo = file.split("-")[0]
    # TODO 使用os.path.join()函数拼接分类文件夹路径，赋值给classPath
    classPath = os.path.join(path,classInfo)

    # TODO 使用os.path.exists()函数判断当如果目标文件夹不存在
    if not os.path.exists(classPath):
        # TODO 使用os.mkdir()函数创建文件夹
        os.mkdir(classPath)

    # TODO 使用os.path.join()函数拼接文件路径，并赋值给变量sourcePath
    sourcePath = os.path.join(path,file)

    # TODO 使用os.path.isdir()函数判断当目标文件不是文件夹
    if not os.path.isdir(sourcePath):
        # TODO 移动文件到分类文件夹去
        shutil.move(sourcePath,classPath)