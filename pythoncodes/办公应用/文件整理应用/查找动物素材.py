# TODO 使用import导入os模块
import os

# TODO 使用import导入shutil模块
import shutil

# TODO 将需要查找的动物文件名称赋值给列表animalList
animalList = ['东北虎.jpg', '非洲最美猎豹.jpg', '非洲最美长颈鹿.jpg', '几维鸟.jpg']

# TODO 将素材的文件路径 '/Users/awen/source' 赋值给path
path = r"d:\source"

# TODO 使用os.listdir()函数获取路径下所有文件名称，并赋值给fileNames
fileNames = os.listdir(path)

# TODO 使用for循环遍历文件名列表fileNames
for file in fileNames:

    # TODO 使用if判断，当文件名在动物列表animalList里面时
    if file in animalList:

        # TODO 使用os.path.join()拼接找到的文件路径，赋值给filePath
        filePath = os.path.join(path,file)

        # TODO 使用os.path.join()拼接要存储的文件路径 '/Users/awen/animal'，赋值给targetPath
        targetPath = r'd:\animal'
        
        # TODO 使用shutil.move()移动文件到targetPath路径下
        shutil.move(filePath,targetPath)

        # TODO 格式化输出 xx已移动到animal文件夹
        print(f"{file}已移动到animal文件夹")
