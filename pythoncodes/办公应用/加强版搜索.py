
# TODO 使用import导入os模块
import os

# 要查询的文件列表
queryList = ["大象洗澡.mp4", "心动.MP3", "河马洗澡.mp4", "长颈鹿洗澡.mp4", "猎豹.jpg"]

# 将阿文的下载文件夹路径 /Users/yequ/Downloads 赋值给变量downloadPath
downloadPath = "/Users/yequ/Downloads"

# TODO 使用os.listdir()函数获取该路径下所有的文件(夹)，并赋值给变量allItems
allItems = os.listdir(downloadPath)

# TODO 遍历所有要查询的文件列表queryList
for file in queryList:
    # TODO 使用in运算符判断当文件存在于allItems时
    if file in allItems:
        # TODO 输出文件名
        print(file)