# TODO 导入os模块
import os

# 所有的学生名字列表
studentList = ["James", "Harry", "Maggie", "Joan", "Judy", "Fred", "Roy", "Billy", "Louis", "Tony", "Kevin", "Tracy", "Vincent", "Jay", "Dean", "Neil", "Faye", "Evan", "Dana", "Kelly"]

# TODO 将路径 /Users/ivy/证件照 赋值给变量photoPath
photoPath = "/Users/ivy/证件照"

# TODO 使用函数os.listdir()获取路径下所有的文件列表并赋值给变量allPhotos
allPhotos = os.listdir(photoPath)

# 定义一个空列表变量lowerSubList
# 用来装已经收到照片同学名字的列表，全小写
lowerSubList = []

# 遍历文件列表
for photo in allPhotos:
    # TODO 使用os.path.splitext()函数分隔后缀名
    # 取第一个元素，也就是姓名的部分赋值给变量name
    name = os.path.splitext(photo)[0]

    # TODO 将name用lower()函数转成小写添加到列表lowerSubList中
    # 需要用到列表的append()函数
    lowerSubList.append(name.lower())

# TODO 定义空列表变量notSubList, 用来放没有提交照片用户的名字
notSubList = []

# 遍历所有学生名字列表
for student in studentList:
    # TODO 将名字用lower()转成小写然后判断当不在已经提交的名单时
    if student.lower() not in lowerSubList:
        # TODO 找到没有提交同学的名字,添加到列表notSubList
        notSubList.append(student)

# TODO 输出notSubList，也就是没有交照片同学的名字
print(notSubList)