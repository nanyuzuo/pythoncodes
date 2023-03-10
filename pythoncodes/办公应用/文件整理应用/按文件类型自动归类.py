# 使用import导入os模块
import os

# TODO 使用import导入shutil模块
import shutil

# 将阿文的下载文件夹路径 /Users/yequ/Downloads 赋值给变量downloadPath
downloadPath = r"C:\Users\will\Downloads"

# 使用os.listdir()函数获取该路径下所有的文件(夹)，并赋值给变量allItems
allItems = os.listdir(downloadPath)

# 使用for循环遍历所有文件(夹)
for item in allItems:
    # 获取文件后缀名
    extension = os.path.splitext(item)[1].lower()

    # 定义一个变量targetPath，用来表示准备移动到的文件夹路径
    targetPath = ""
    if extension in [".jpg", ".jpeg", ".gif", ".png", ".bmp"]:
        # 使用os.path.join()函数拼接分类文件夹路径：图片文件
        targetPath = os.path.join(downloadPath, "图片文件")
    elif extension in [".avi", ".mp4", ".wmv", ".mov", ".flv"]:
        # 使用os.path.join()函数拼接分类文件夹路径：视频文件
        targetPath = os.path.join(downloadPath, "视频文件")
    elif extension in [".wav", ".mp3", ".mid", ".ape", ".flac"]:
        # 使用os.path.join()函数拼接分类文件夹路径：音频文件
        targetPath = os.path.join(downloadPath, "音频文件")
    elif extension in [".pdf"]:
        # 使用os.path.join()函数拼接分类文件夹路径：PDF文件
        targetPath = os.path.join(downloadPath, "PDF文件")
    elif extension in [".docx", ".doc"]:
        # 使用os.path.join()函数拼接分类文件夹路径：Word文件
        targetPath = os.path.join(downloadPath, "Word文件")
    elif extension in [".xlsx", ".xls"]:
        # 使用os.path.join()函数拼接分类文件夹路径：Excel文件
        targetPath = os.path.join(downloadPath, "Excel文件")
    elif extension in [".pptx", ".ppt"]:
        # 使用os.path.join()函数拼接分类文件夹路径：PPT文件
        targetPath = os.path.join(downloadPath, "PPT文件")
    elif extension in [".rar", ".zip",".bz","gz"]:
        # 使用os.path.join()函数拼接分类文件夹路径：PPT文件
        targetPath = os.path.join(downloadPath, "压缩包文件")
    elif extension in [".exe", ".bat",".com",".msi"]:
        # 使用os.path.join()函数拼接分类文件夹路径：PPT文件
        targetPath = os.path.join(downloadPath, "可执行文件")
    else:
        # 使用os.path.join()函数拼接分类文件夹路径：其他文件
        targetPath = os.path.join(downloadPath, "其他文件")
    # 如果目标文件夹不存在，使用os.mkdir()函数创建文件夹
    if not os.path.exists(targetPath):
        os.mkdir(targetPath)

    # 使用os.path.join()函数拼接文件路径，并赋值给变量itemPath
    itemPath = os.path.join(downloadPath, item)

    # TODO 使用os.path.isdir()函数判断当itemPath不是文件夹时。
    if not os.path.isdir(itemPath):
        # TODO 使用shutil.move()函数移动文件到targetPath路径
        shutil.move(itemPath,targetPath)