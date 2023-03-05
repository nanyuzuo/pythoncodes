# TODO 使用import导入os模块
import os
# TODO 使用import导入shutil模块
import shutil

# 定义一个将文件从所有文件中取出的函数findAllFiles
# 需要查找的文件路径参数filePath，移动目标路径targetPath
def findAllFiles(filePath, targetPath):
    
    # TODO 使用os.listdir()获取路径下所有文件和文件夹名称
    allItems = os.listdir(filePath)

    # TODO 循环遍历allItems列表中所有文件(夹)名称
    for file in allItems:
        
        # TODO 使用os.path.join()合并每个文件(夹)的路径，赋值给itemPath
        itemPath = os.path.join(filePath,file)

        # TODO 使用if语句判断 itemPath 路径是一个文件夹时
        if os.path.isdir(itemPath):
            # TODO 递归调用此函数，找到文件夹下的所有文件,移动到目标路径
            findAllFiles(itemPath,targetPath)

        # TODO 不是文件夹就是文件
        else:
            
            shutil.move(itemPath,targetPath)

# 使用findAllFiles函数查找路径下 /Users/Desktop/awen 的所有文件，移动到 /Users/Desktop/rearrange 文件夹中
findAllFiles('/Users/Desktop/awen', '/Users/Desktop/rearrange')