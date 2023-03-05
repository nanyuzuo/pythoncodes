# TODO 使用import导入os模块
import os
# TODO 使用import导入ezexif模块
import ezexif
# TODO 使用import导入shutil模块
import shutil

# TODO 将要找照片文件路径 /Users/taxi/照片 赋值给变量path
path = "/Users/taxi/照片"

# TODO 使用os.listdir()函数获取该路径下所有的文件(夹)，并赋值给变量fileNames
fileNames = os.listdir(path)

# TODO 使用for循环遍历所有文件(夹)
for file in fileNames:

    # TODO 使用os.path.join()函数拼接查找照片路径，并赋值给变量filePath
    filePath = os.path.join(path,file)

    # TODO 使用ezexif.process_file()获取exif信息，并赋值给exifInfo
    exifInfo = ezexif.process_file(filePath)

    # TODO 使用exifInfo['EXIF DateTimeOriginal']获取拍摄时间，并赋值给takeTime
    takeTime = exifInfo['EXIF DateTimeOriginal']
    
    # TODO 使用split()通过空格分隔成拍摄日期和拍摄时间，并赋值给takeTimeParts
    takeTimeParts = takeTime.split(" ")
    
    # TODO 分隔后的字符串列表第一个元素就是拍摄日期，赋值给变量photoDate
    photoData =  takeTimeParts[0]
    
    # TODO 再把拍摄日期通过冒号分隔，分成年、月、日三部分，赋值给变量photoDateParts
    photoDateParts = photoData.split(":")
    
    # TODO 分隔后的字符串列表第一个元素就是拍摄年份，赋值给变量year
    year = photoDateParts[0]
    
    # TODO 分隔后的字符串列表第二个元素就是拍摄月份，赋值给变量month
    month = photoDateParts[1]

    # TODO 使用if找到同时满足拍摄年份为2015年，拍摄月份为10月的照片
    if year == "2015" and month == "10":
    
        # TODO 使用os.path.join()函数拼接2015年10月的照片路径 '/Users/taxi/2015年'，并赋值给变量targetPath
        targetPath = os.path.join("/Users/taxi/2015年",file)
        
        # TODO 使用shutil.copy()复制照片到目标文件夹中
        shutil.copy(filePath,targetPath)
        