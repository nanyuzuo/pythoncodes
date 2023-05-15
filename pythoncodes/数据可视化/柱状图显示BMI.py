# TODO 使用from...import从pyecharts中导入options模块并简写为opts
from pyecharts import options as opts

# TODO 使用from...import从pyecharts.charts中导入Bar模块
from pyecharts.charts import Bar

# TODO 使用Bar()函数创建对象并赋值给变量bar
bar = Bar()

# 将5位同学的姓名存入变量名为'name'的列表中
name = ["yoyo","coco","jojo","momo","bobo"]

# 按照同学姓名的顺序，依次将同学的身高存入变量名为'height'的列表中
height = [1.55, 1.60, 1.58, 1.68, 1.65]

# 按照同学姓名的顺序，依次将同学的体重存入变量名为‘weight’的列表中
weight = [45, 50, 48, 55, 49]

# TODO 定义一个空列表BMIList，用于存储BMI信息
BMIList = [ round(a/(b*b)) for a,b in zip(weight,height) ]

# TODO 传入参数xaxis_data=name使用add_xaxis()设置x轴为姓名
bar.add_xaxis(name)

# TODO 传入参数y_axis=BMIList使用add_yaxis()设置y轴，series_name为空
bar.add_yaxis(series_name='',y_axis=BMIList)

# TODO 初始化一个TitleOpts对象，设置标题名称为"BMI数据统计"，并将其赋值给变量title_options
title_options = opts.TitleOpts(title="BMI数据统计")

# TODO 使用set_global_opts进行标题配置，标题配置项的值为title_options
bar.set_global_opts(title_opts=title_options)

# TODO 使用render()绘制出柱状图"/Users/bmi.html"
bar.render("d:\\yequ\\test\\bmi.html")