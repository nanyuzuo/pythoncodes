# TODO 导入os模块
import os

# TODO 导入ezexif模块
import ezexif

# TODO 导入shutil模块
import shutil

# TODO 将照片文件夹路径 /Users/yequ/Desktop/picture 赋值给path
path = "/Users/yequ/Desktop/picture"

# TODO 使用os.path.join()函数拼接path和文件夹名"素材",赋值给变量resourcePath
resourcePath = os.path.join(path,"素材")

# TODO 使用os.path.exists()函数判断当如果目标文件夹不存在
if not os.path.exists(resourcePath):
    # TODO 使用os.mkdir()函数创建文件夹
    os.mkdir(resourcePath)

# TODO 使用os.path.join()函数拼接path和文件夹名"修改",赋值给变量revisePath
revisePath = os.path.join(path,"修改")

# TODO 使用os.path.exists()函数判断当如果目标文件夹不存在
if not os.path.exists(revisePath):
    # TODO 使用os.mkdir()函数创建文件夹
    os.mkdir(revisePath)

# TODO 使用os.listdir()函数获取path路径下所有的文件(夹)，并赋值给变量photoList
photoList = os.listdir(path)

# TODO 使用for循环遍历所有文件(夹)
for photo in photoList:
    # TODO 使用os.path.join()函数拼接path和文件名，赋值给变量photoPath
    photoPath = os.path.join(path,photo)

    # TODO 使用函数os.path.isdir()判断当photoPath不是文件夹时
    if not os.path.isdir(photoPath):
        # TODO 获取exif信息，赋值给变量exifInfo
        exifInfo = ezexif.process_file(photoPath)

        # TODO 获取照片长度，赋值给变量imageLeng
        imageLeng = exifInfo["EXIF ExifImageLength"]
        # TODO 获取照片宽度，赋值给变量imageWidth
        imageWidth = exifInfo["EXIF ExifImageWidth"]

        # TODO 如果整型imageLeng和整型imageWidth都比60小
        if int(imageLeng) < 60 and int(imageWidth) < 60:
            # TODO 转移图片到素材文件夹
            shutil.move(photoPath,resourcePath)
        # TODO 否则
        else:
            # TODO 转移图片到修改文件夹
            shutil.move(photoPath,revisePath)
            
# TODO print输出success
print("success")