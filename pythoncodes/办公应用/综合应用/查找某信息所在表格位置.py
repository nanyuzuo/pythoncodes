# 从历年的作者投稿登记表中，找到小夜作者的信息登记，查看审稿费缴纳情况。
# 姓名：小夜
# 文章题目：索引
# 邮箱：16798429@yequ.com
# 作者投稿文件存储路径: /Users/year/sub
# 该路径中有三个作者投稿登记表，分别是：
# 作者投稿-18年.xlsx
# 作者投稿-19年.xlsx
# 作者投稿-20年.xlsx
# 每个工作簿中都有12个工作表，并按照1月、2月、3月等方式命名。
# 最后用print(工作簿名称， 行信息)的方式，输出小夜的信息所在的工作簿名称和行信息。

# TODO 使用import导入openpyxl模块
import openpyxl

# TODO 使用import导入os模块
import os

# TODO 将作者投稿的文件夹路径'/Users/year/sub'赋值给path
path = "/Users/year/sub"

# TODO 使用for..in['18年', '19年', '20年']读取三年的作者投稿数据
for year in ['18年','19年','20年']:

    # TODO 利用格式化字符串拼接Excel‘作者投稿-xx.xlsx’文件路径，赋值给fileName
    fileName = f"作者投稿-{year}.xlsx"

    # TODO 使用os.path.join()拼接Excel文件存储路径,赋值给filePath
    filePath = os.path.join(path,fileName)

    # TODO 使用openpyxl.load_workbook()打开作者投稿工作簿，赋值给wb
    wb = openpyxl.load_workbook(filePath)

    # TODO 使用range()函数循环遍历数字1到12
    for i in range(1,13):

        # TODO 利用格式化字符串将每月的工作表名称赋值给month
        month = wb[f"{i}月"]

        # TODO for循环rowData遍历每月的行数据month.rows
        for rowData in month.rows:

            # TODO 获取第1列索引为0的文章题目的值，赋值给title
            title = rowData[0].value

            # TODO 获取第2列索引为1的姓名的值，赋值给name
            name = rowData[1].value

            # TODO 获取第4列索引为3的邮箱的值，赋值给email
            email = rowData[3].value

            # TODO 使用if语句比较题目、姓名和邮箱同时满足的作者信息时
            if ( name == "小夜" ) and ( title == "索引" ) and ( email == "16798429@yequ.com" ):

                # TODO 输出想要查找信息的文档名称fileName和具体位置rowData
                print(fileName, rowData)
                