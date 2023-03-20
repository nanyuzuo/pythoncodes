# TODO 使用import导入os模块
import os

# TODO 将PDF文件夹路径 /Users/yequ/Desktop/PythonCourse，赋值给变量path
path = "/Users/yequ/Desktop/PythonCourse"

# TODO 使用os.listdir()函数获取该路径下所有的文件名称，并赋值给变量allItems
allItems = os.listdir(path)

# TODO 定义新函数sortFile，包含参数fileName
def sortFile(fileName):

    # TODO 使用split()函数，根据"-"分割文件名，获取第二个元素，赋值给sourceName
    sourceName = fileName.split("-")[1]
    # TODO 接着使用split()函数，根据"."分割，获取第一个元素，赋值给变量name
    name = sourceName.split(".")[0]

    # TODO 将name转换成整型后返回
    return int(name)

# TODO 将文件列表allItems中的元素，传入函数sortFile，使用sort()函数排序后输出allItems
allItems.sort(key = sortFile)
print(allItems)        
