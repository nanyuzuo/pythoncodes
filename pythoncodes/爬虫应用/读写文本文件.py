# TODO 创建一个空列表studentNames用来存放家访学生名字
studentNames = []

# TODO 创建一个计数器count初始值为0，用来计数学生人数
count = 0

# TODO 使用with open()函数打开学生名单name_list.txt
# 打开方式设为只读r，将文件名设为f
with open("name_list.txt","r") as f:

    # TODO 使用for循环遍历文件f
    for line in f:

        # TODO 使用if判断当计数器大于等于500时
        if count >= 500:
            # TODO 使用break结束循环
            break

        # TODO 使用append()函数将每一行的数据追加到studentNames列表中
        studentNames.append(line)

        # TODO 计数器count加一
        count = count + 1

# TODO 使用with open()函数打开要存入的家访学生名单visitNames.txt
# 打开方式设为只写w，将文件名设为f
with open("visitNames.txt","w") as f:

    # TODO 使用for循环遍历家访学生列表
    for item in studentNames:

        # TODO 使用write()函数，将每一个学生名字写入
        f.write(item)