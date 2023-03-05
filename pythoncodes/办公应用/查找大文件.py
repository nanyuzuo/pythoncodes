# TODO 使用import导入os模块
import os

# TODO 定义一个函数findBigFiles找文件夹及其子文件夹下的大文件
# 该函数接受一个参数dirPath，即需要查找的文件夹路径
def findBigFiles(dirPath):
    # TODO 使用os.listdir()函数获取该文件夹路径下所有的文件(夹)的名称
    # 并赋值给变量allItems
    allItems= os.listdir(dirPath)

    # 循环遍历所有文件(夹)名称
    for item in allItems:
        # TODO 使用os.path.join()函数合并生成每个文件(夹)的路径并赋值给itemPath
        itemPath = os.path.join(dirPath,item)

        # TODO 使用os.path.isdir()函数判断当itemPath该路径下是一个文件夹时
        if os.path.isdir(itemPath):
            # TODO 递归调用此函数，找这个文件夹及其子文件夹下的大文件
            findBigFiles(itemPath)
        # TODO 其他情况，也就是itemPath是文件的话
        else:
            # TODO 通过os.path.getsize()函数获取文件大小并赋值给变量fileSize
            fileSize = os.path.getsize(itemPath)
            # TODO 如果文件大小大于2000字节
            if fileSize > 2000:
                # TODO 使用print输出文件路径itemPath
                print(itemPath)

# 使用findBigFiles函数查找路径"/Users/Yoyo"下的大文件
findBigFiles("/Users/Yoyo")