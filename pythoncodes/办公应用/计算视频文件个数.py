# TODO 使用import导入os模块
import os

# TODO 将路径 /Users/yequ/doc 赋值给变量docPath
docPath = "/Users/yequ/doc"

# TODO 使用os.listdir()函数获取该路径下所有的文件(夹)，并赋值给变量allItems
allItems = os.listdir(docPath)

# 定义一个视频计数变量videoCount
videoCount = 0

# TODO 使用for循环遍历所有文件(夹)
for file in allItems:
    # TODO 使用os.path.splitext()函数获取文件后缀名，赋值给变量extension
    extension = os.path.splitext(file)[1]

    # TODO 根据后缀名判断是视频文件，计数变量就+1
    if extension in [".avi",".mp4",".wmv",".flv"]:
        videoCount = videoCount + 1
        

# TODO 输出题目要求格式的结果
print(f"一共有{videoCount}个视频文件")