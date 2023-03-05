# TODO 使用 import 导入os模块
import os

# TODO 定义一个函数searchFile用来搜索路径下指定大小的文件
# 参数 searchPath: 搜索文件的起始路径
# 参数 fileSize: 指定文件的大小，单位是字节
def searchFile(searchPath,fileSize):
    # TODO 使用os.listdir()函数获取路径下所有文件并赋值给allItems
    allItems = os.listdir(searchPath)

    # TODO 遍历所有文件allItems
    for item in allItems:
        # TODO 使用os.path.join()函数合并文件路径并赋值给变量itemPath
        itemPath = os.path.join(searchPath,item)

        # TODO 使用os.path.isdir()函数判断当itemPath路径是一个文件夹时
        if os.path.isdir(itemPath):
            # TODO 又变成了去文件夹搜索文件, 递归调用函数searchFile
            searchFile(itemPath,fileSize)
        # TODO 其他情况，也就是文件时
        else:
            # TODO 使用os.path.getsize()函数获取文件大小并赋值给变量size
            size = os.path.getsize(itemPath)

            # TODO 判断当查询的大小和搜索的文件大小相等时
            if size == fileSize:
                # TODO 输出文件路径
                print(itemPath)

# TODO 使用searchFile函数查询路径 /Users/y11 下大小为96592字节的文件
searchFile("/Users/y11",96592)