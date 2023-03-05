# TODO 使用import导入os模块
import os

# TODO 将阿文的下载文件夹路径 /Users/yequ/Downloads 赋值给变量downloadPath
downloadPath = "/Users/yequ/Downloads"

# TODO 使用os.listdir()函数获取该路径下所有的文件(夹)，并赋值给变量allItems
allItems = os.listdir(downloadPath)

# 设置布尔变量hasFound用于判断是否找到文件, 初始值为False
hasFound = False

# TODO 使用for循环遍历所有文件(夹)
for file in allItems:
    # TODO 判断当文件是 夜曲编程笔记.docx 时
    if file == "夜曲编程笔记.docx":
        # TODO 将 hasFound 赋值为True, 表示文件已经找到
        hasFound = True

# TODO 判断当hasFound为True时
if hasFound:
    # TODO 输出: 夜曲编程笔记文档在文件夹中
    print("夜曲编程笔记文档在文件夹中")
# TODO 其他情况时
else:
    # TODO 输出: 夜曲编程笔记文档不在文件夹中
    print("夜曲编程笔记文档不在文件夹中")
