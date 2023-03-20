# TODO 使用import导入os模块
import os

# TODO 将PDF文件夹路径 /Users/yequ/Desktop/PythonCourse，赋值给变量path
path = r"d:\test\PythonCourse"

# TODO 使用os.listdir()函数获取该路径下所有的文件名称，并赋值给变量allItems
allItems = os.listdir(path)

# TODO 新建一个空白列表chapterList
chapterList = []

# TODO 使用for循环遍历allItems
for item in allItems:
    # TODO 使用split()函数，根据"-"分割文件名，获取第二个元素，赋值给fullName
    fullName = item.split("-")[1]
    # TODO 接着使用split()函数，根据"."分割，获取第一个元素，赋值给变量name
    name = fullName.split(".")[0]

    # TODO 将name添加进列表chapterList
    chapterList.append(name)

# TODO 使用sort()函数，将列表chapterList中的元素以数字类型排序
chapterList.sort(key = int)

# TODO 新建一个空白列表file
file = []

# TODO 使用for循环遍历chapterList
for i in chapterList:
    # TODO 使用for循环遍历allItems,找到文件列表中对应的文件
    for item in allItems:

        # TODO 赋值给newChapter
        newChapter = i
        
        # TODO 使用split()函数，根据"-"分割获取第二个元素，赋值给变量sourceName
        sourceName = item.split("-")[1]
        # TODO 接着使用split()函数，根据"."分割，获取第一个元素，赋值给变量newName 
        newName = sourceName.split(".")[0]
        
        # TODO 判断变量newChapter与newName是否相等
        if newChapter == newName:
        
            # TODO 将item添加进列表file
            file.append(item)

# TODO 使用print输出列表file
print(file)