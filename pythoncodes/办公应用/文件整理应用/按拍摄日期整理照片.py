# 导入os模块
import os

# 导入ezexif模块,需要首先用pip install ezexif安装
import ezexif

# 导入shutil模块
import shutil

currentPath = os.getcwd()

os.chdir(currentPath)

# 将待处理照片的相对路径赋值给backupPhotoPath
backupPhotoPath = "照片"

# 使用函数os.listdir()获取所有待处理照片文件列表
photoList = os.listdir(backupPhotoPath)

# 遍历文件列表
for photo in photoList:
    # 使用os.path.join()函数组合得到照片文件路径，并赋值给变量photoPath
    photoPath = os.path.join(backupPhotoPath, photo)
    # 获取exif信息
    exifInfo = ezexif.process_file(photoPath)
    # 获取拍摄时间
    takeTime = exifInfo["EXIF DateTimeOriginal"]
    # 通过空格分隔成拍摄日期和拍摄时间
    takeTimeParts = takeTime.split(" ")
    # 分隔后的字符串列表第一个元素就是拍摄日期，赋值给变量photoDate
    photoDate = takeTimeParts[0]
    # 再把拍摄日期通过冒号分隔，分成年、月、日三部分，赋值给变量photoDateParts
    photoDateParts = photoDate.split(":")

    # 利用格式化字符串拼出文件夹名称
    targetFolderName = f"{photoDateParts[0]}年{photoDateParts[1]}月"
    # 使用os.path.join()函数拼出分类文件夹的路径, 并赋值给photoTargetPath变量
    photoTargetPath = os.path.join(backupPhotoPath, targetFolderName)

    # 如果目标文件夹不存在，使用os.mkdir()函数创建文件夹
    if not os.path.exists(photoTargetPath):
        os.mkdir(photoTargetPath)

    # 移动到目标文件夹
    shutil.move(photoPath, photoTargetPath)