# TODO 使用from..import..导入PIL模块中的Image
from PIL import Image

# TODO 使用import导入os模块
import os

# TODO 将图片文件路径"/Users/img/before"，赋值给path
path = "/Users/img/before"

# TODO 使用os.listdir()获取路径下的所有图片,赋值给photoNames
photoNames = os.listdir(path)

# TODO 使用for循环遍历所有的文件名
for photo in photoNames:

    # TODO 使用os.path.join()拼接图片路径，赋值给filePath
    filePath = os.path.join(path,photo)

    # TODO 使用Image.open()打开图片文件，赋值给imgBefore
    imgBefore = Image.open(filePath)

    # TODO 定义一个变量width表示图片宽度，为295
    width = 295

    # TODO 定义一个变量height表示图片高度，为413
    height = 413

    # TODO 使用.resize((width, height))修改图片尺寸，修改后赋值给imgAfter
    imgAfter = imgBefore.resize((width,height))
    
    # TODO 使用save()函数，用原文件名保存至 /Users/img/after 路径下
    imgAfter.save(f"/Users/img/after/{photo}")