# TODO 导入os模块
import os

# TODO 导入shutil模块
import shutil

# TODO 将路径 /Users/ming/素材 赋值给变量audioPath
audioPath = "/Users/ming/素材"

# TODO 使用os.listdir()函数获取所有文件列表并赋值给变量allAudio
allAudio = os.listdir(audioPath)

# 输出更名前的所有文件名allAudio
print(allAudio)

# 遍历所有音频文件
for audio in allAudio:
    # TODO 使用replace()函数在文件名中去掉[夜曲资源网]
    # 第二个参数传入空字符串达到删除效果
    newAudio = audio.replace("[夜曲资源网]","")

    # TODO 使用os.path.join()函数合并更名前路径并赋值给变量oldPath
    oldPath = os.path.join(audioPath,audio)
    # TODO 使用os.path.join()函数合并更名后路径并赋值给变量newPath
    newPath = os.path.join(audioPath,newAudio)

    # TODO 将oldPath和newPath传入shutil.move()函数重命名文件
    shutil.move(oldPath,newPath)

# 使用os.listdir()函数重新获取路径下所有文件赋值给变量newAllAudio
newAllAudio = os.listdir(audioPath)

# 输出更名后的所有文件名newAllAudio
print(newAllAudio)