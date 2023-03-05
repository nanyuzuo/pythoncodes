# TODO 使用import导入os模块
import os

# TODO 使用import导入shutil模块
import shutil

# TODO 使用os.chdir()修改当前工作目录到/Volumes/backup
os.chdir("/Volumes/backup")

# TODO 将要整理的学生信息文件夹的相对路径赋值给变量backupStuPath
backupStuPath = "学生信息"

# TODO 使用os.listdir()函数获取该路径下所有的文件(夹)，并赋值给变量allItems
allItems = os.listdir(backupStuPath)

# TODO 使用for循环遍历所有文件(夹)
for item in allItems:

    # TODO 取学号的第5和第6个字符并赋值给变量stuClass，提取学生班级
    stuClass = item[4:6]

    # TODO 使用格式化字符串拼接分类文件夹名字:{stuClass}班, 并赋值给变量folderName
    folderName = f"{stuClass}班"

    # TODO 使用os.path.join()函数拼接分类文件夹路径，并赋值给变量targetPath
    targetPath = os.path.join(backupStuPath,folderName)

    # TODO 判断当如果目标文件夹不存在
    if not os.path.exists(targetPath):
        # TODO 使用os.mkdir()函数创建文件夹
        os.mkdir(targetPath)

    # TODO 使用os.path.join()函数拼接文件路径，并赋值给变量itemPath
    itemPath = os.path.join(backupStuPath,item)

    # TODO 判断当itemPath不是文件夹时
    if not os.path.isdir(itemPath):
        # TODO 使用shutil.move()函数移动文件到targetPath路径
        shutil.move(itemPath,targetPath)
