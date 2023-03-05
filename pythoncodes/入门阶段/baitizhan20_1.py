# 导入模块random
import random
# 定义包含课程名的列表
course = ['办公自动化', '数据分析基础', '数据分析进阶','网络爬虫', '数据可视化', 'SQL数据处理','人工智能应用','趣味工具','网页开发']
# 定义总次数times
times = 1000
# 定义计数的变量count
count = 0

# TODO for循环遍历1000次
for i in range(times):
    # TODO 随机从列表中选择一门课程，赋值给courseMing
    courseMing = course[random.randint(0,8)]
    # TODO 随机从列表中选择一门课程，赋值给courseLi
    courseLi = random.choice(course)
    # TODO 判断小明和小李选择的课程是否相同，相同则count自加1
    if courseMing == courseLi:
        count = count + 1
        
# TODO 输出count/times
rate = count / times
print(rate)