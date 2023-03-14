# TODO 使用import导入os模块
import os

# TODO 使用import导入shutil模块
import shutil

# 将筛选后的报名表路径 /Users/yequ/Downloads/registration 赋值给变量allFormPath
allFormPath = "/Users/yequ/Downloads/registration"

# 使用os.listdir()函数获取该路径下所有的报名表，并赋值给变量allItems
allItems = os.listdir(allFormPath)

# TODO 使用print输出变量allItems
print(allItems)

# 使用for循环逐个遍历所有报名表
for item in allItems:
    # 使用os.path.join()函数合并路径并赋值给变量path
    path = os.path.join(allFormPath, item)
    # 使用os.path.splitext()函数获取文件名的前半段，并赋值给变量fileName
    fileName = os.path.splitext(item)[0]
    # 使用split()函数以"-"分隔文件名，并赋值给变量result
    result = fileName.split("-")

    # TODO 读取变量result中的第2个元素【意愿科目】，并赋值给变量targetSubject
    targetSubject = result[1]

    # TODO 使用os.path.join()函数拼接文件夹路径，并赋值给变量targetSubjectPath
    targetSubjectPath = os.path.join(allFormPath,targetSubject)

    # TODO 使用os.path.exists()判断目标文件夹是否不存在
    if not os.path.exists(targetSubjectPath):

        # TODO 如果不存在，则使用os.mkdir()函数创建对应文件夹
        os.mkdir(targetSubjectPath)

    # TODO 使用shutil.move()函数将报名表移动到对应文件夹中
    shutil.move(path,targetSubjectPath)

# TODO 使用os.listdir()函数获取现在 allFormPath 路径下的所有文件夹，并赋值给变量updateItems
updateItems = os.listdir(allFormPath)

# TODO 使用print输出变量updateItems
print(updateItems)